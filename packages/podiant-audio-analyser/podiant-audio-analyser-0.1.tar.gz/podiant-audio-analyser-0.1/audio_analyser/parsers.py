from .exceptions import AnalysisError
import re


FRAME_LINE_REGEX = r'frame:(\d+) *pts:(\d+) *pts_time:([\d+\.]+) *$'
RMS_LINE_REGEX = r'lavfi\.astats\.Overall\.RMS_level=([^ ]+) *$'


def rms(line, bucket, callback):
    frame_match = re.search(FRAME_LINE_REGEX, line)
    if frame_match is not None:
        frame, pts, time = frame_match.groups()

        try:
            frame = int(frame)
            pts = int(pts)
            time = float(time)
        except Exception:
            raise AnalysisError(
                'Frame data is invalid.',
                frame_match.groups()
            )

        if frame in bucket:
            raise AnalysisError(
                'Received frame data while still waiting for RMS level.'
            )

        bucket[frame] = {
            'pts': pts,
            'time': time
        }

        return

    rms_match = re.search(RMS_LINE_REGEX, line)
    if rms_match is not None:
        level = rms_match.groups()[0]

        try:
            level = float(level)
        except Exception:
            raise AnalysisError('RMS data is invalid.', level)

        try:
            last_frame_key = list(reversed(sorted(bucket.keys())))[0]
        except IndexError:
            raise AnalysisError('Could not tie RMS data to a frame.')

        last_frame = bucket[last_frame_key]
        if 'level' in last_frame:
            raise AnalysisError(
                'Already received RMS data for frame %s.' % last_frame_key
            )

        bucket[last_frame_key]['level'] = level
        callback(bucket[last_frame_key])

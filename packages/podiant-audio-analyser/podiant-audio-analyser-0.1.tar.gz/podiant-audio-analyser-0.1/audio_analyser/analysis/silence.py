from .base import AnalyserBase
import time


NOISE_FLOOR = -100
MAX_ALLOWABLE_SILENCE = 5


class OpeningSilenceAnalyser(AnalyserBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_allowable = MAX_ALLOWABLE_SILENCE
        self.noise_floor = NOISE_FLOOR
        self.peaks = []

    def read_chunk(self, offset, data):
        done = False

        for slice in data:
            level = slice['level']
            if level >= self.noise_floor:
                done = True
                break

            self.peaks.append(level)

        if (offset + 1) >= self.max_allowable:
            self.check_silence()
            done = True

        if done:
            self.done()

    def check_silence(self):
        peaks = sum(self.peaks)
        if peaks <= self.noise_floor:
            self.report(
                title='Too quiet at start',
                description=(
                    'There are more than %s seconds of silence at the '
                    'beginning of this file.'
                ) % self.max_allowable
            )


class TrailingSilenceAnalyser(AnalyserBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_allowable = MAX_ALLOWABLE_SILENCE
        self.noise_floor = NOISE_FLOOR
        self.offset = 0
        self.unbroken_silence = 0

    def read_chunk(self, offset, data):
        silence_in_chunk = False

        for slice in data:
            level = slice['level']
            if level >= self.noise_floor:
                self.unbroken_silence = 0
                return

            silence_in_chunk = True

        if silence_in_chunk:
            self.unbroken_silence += 1

    def finish(self):
        if self.unbroken_silence >= self.max_allowable:
            self.report(
                title='Too quiet at end',
                description=(
                    'There are roughly %s seconds of silence at the end of '
                    'this file.'
                ) % self.unbroken_silence,
                duration=self.unbroken_silence
            )


class GapAnalyser(AnalyserBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_allowable = MAX_ALLOWABLE_SILENCE * 2
        self.noise_floor = NOISE_FLOOR
        self.offset = 0
        self.peaks = []
        self.unbroken_silence = 0
        self.silence_broken = False

    def read_chunk(self, offset, data):
        silence_in_chunk = False

        for slice in data:
            level = slice['level']
            if level >= self.noise_floor:
                if self.unbroken_silence >= self.max_allowable:
                    if self.silence_broken:
                        self.report_silence(offset)

                self.unbroken_silence = 0
                self.silence_broken = True

            silence_in_chunk = True

        if silence_in_chunk:
            self.unbroken_silence += 1

    def report_silence(self, offset):
        self.report(
            title='Long period of silence',
            description=(
                'There is a roughly %s-second period of silence at %s'
            ) % (
                self.unbroken_silence,
                time.strftime('%H:%M:%S', time.gmtime(offset))
            ),
            offset=offset,
            duration=self.unbroken_silence
        )

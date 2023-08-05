from .base import AnalyserBase


LOUDNESS_THRESHOLD = -16
LOUDNESS_GRACE = 8


class LoudnessAnalyser(AnalyserBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threshold = LOUDNESS_THRESHOLD
        self.grace = LOUDNESS_GRACE

    def summarise(self, data):
        loudness = data.get('loudness')
        if loudness is not None:
            if loudness > self.threshold:
                self.check_too_loud(loudness)
            elif loudness < self.threshold:
                self.check_too_quiet(loudness)

    def check_too_quiet(self, loudness):
        delta = self.threshold - loudness

        if delta >= self.grace:
            self.report(
                title='Too quiet overall',
                description=(
                    'Your audio file is fairly quiet overall, averaging'
                    'at %s LUFS. The standard recommendation is to have '
                    'audio normalized to %s LUFS.'
                ) % (
                    loudness,
                    self.threshold
                ),
                level=loudness
            )

    def check_too_loud(self, loudness):
        delta = loudness - self.threshold

        if delta >= self.grace:
            self.report(
                title='Too loud overall',
                description=(
                    'Your audio file is fairly loud overall, averaging'
                    'at %s LUFS. The standard recommendation is to have '
                    'audio normalized to %s LUFS.'
                ) % (
                    loudness,
                    self.threshold
                ),
                level=loudness
            )

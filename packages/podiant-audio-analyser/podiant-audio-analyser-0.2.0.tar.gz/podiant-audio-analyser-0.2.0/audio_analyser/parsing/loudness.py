from ..exceptions import AnalysisError
from .base import ParserBase
import re


LUFS_REGEX = r'^ *I\: *([\d+\.-]+) LUFS$'


class LoudnessParser(ParserBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._has_summary = False
        self._loudness_ready = False
        self._finished = False

    def parse(self, line):
        if self._finished:
            return

        if not self._has_summary:
            if 'Summary:' in line:
                self._has_summary = True

            return

        match = re.search(LUFS_REGEX, line)
        if match is not None:
            if not self._loudness_ready:
                raise AnalysisError(
                    'Received LUFS data while still waiting for '
                    'section heading.'
                )

            lufs = float(match.groups()[0])
            self._emit(
                'summary',
                {
                    'loudness': lufs
                }
            )

            self._finished = True
        elif self._loudness_ready:
            raise AnalysisError(
                'Expected loudness data after section heading.'
            )
        elif 'Integrated loudness:' in line:
            if not self._has_summary:
                raise AnalysisError(
                    'Expected integrated loudness section to follow summary.'
                )

            self._loudness_ready = True

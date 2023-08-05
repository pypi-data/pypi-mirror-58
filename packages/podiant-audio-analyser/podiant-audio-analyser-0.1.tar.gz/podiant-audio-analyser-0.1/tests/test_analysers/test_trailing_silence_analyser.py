from audio_analyser import analyse, reporting
import os
import pytest


FIXTURES = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    ),
    'fixtures'
)


def test_trailing_silence_analyser():
    reporter = reporting.TestReporter()
    filename = os.path.join(FIXTURES, 'trailing_silence.mp3')
    analyse(filename, reporter)

    for item in reporter.data:
        if item['reporter'] == 'trailing-silence':
            assert item['duration'] == 5
            return

    pytest.fail('Trailing silence not detected')

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


def test_opening_silence_analyser():
    reporter = reporting.TestReporter()
    filename = os.path.join(FIXTURES, 'opening_silence.mp3')
    analyse(filename, reporter)

    for item in reporter.data:
        if item['reporter'] == 'opening-silence':
            return

    pytest.fail('Opening silence not detected')

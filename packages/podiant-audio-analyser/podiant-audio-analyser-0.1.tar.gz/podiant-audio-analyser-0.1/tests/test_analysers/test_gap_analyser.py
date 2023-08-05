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


def test_gap_analyser():
    reporter = reporting.TestReporter()
    filename = os.path.join(FIXTURES, 'gap.mp3')
    analyse(filename, reporter)

    for item in reporter.data:
        if item['reporter'] == 'gap':
            assert item['offset'] == 13
            assert item['duration'] == 10
            return

    pytest.fail('Trailing silence not detected')

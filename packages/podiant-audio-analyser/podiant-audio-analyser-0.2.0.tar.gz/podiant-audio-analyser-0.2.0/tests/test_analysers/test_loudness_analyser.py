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


def test_loudness_analyser_quiet():
    reporter = reporting.TestReporter()
    filename = os.path.join(FIXTURES, 'quiet.mp3')
    analyse(filename, reporter)

    for item in reporter.data:
        if item['reporter'] == 'loudness':
            assert item['level'] == -24
            return

    pytest.fail('Incorrect loudness level not detected')


def test_loudness_analyser_loud():
    reporter = reporting.TestReporter()
    filename = os.path.join(FIXTURES, 'loud.mp3')
    analyse(filename, reporter)

    for item in reporter.data:
        if item['reporter'] == 'loudness':
            assert item['level'] == -1.2
            return

    pytest.fail('Incorrect loudness level not detected')

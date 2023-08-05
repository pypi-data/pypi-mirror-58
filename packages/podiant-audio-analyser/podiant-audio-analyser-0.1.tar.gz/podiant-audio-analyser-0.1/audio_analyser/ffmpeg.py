from logging import getLogger
from .exceptions import AnalysisError, ConfigurationError
import os
import subprocess


FFMPEG_PATH = os.getenv('FFMPEG_PATH', '/usr/local/bin/ffmpeg')


def run(*args, **kwargs):
    parse = kwargs.pop('parser', lambda a, b, c: None)
    interpreter = kwargs.pop('interpreter')
    logger = getLogger('audio_analyser')

    if not os.path.exists(FFMPEG_PATH):  # pragma: no cover
        raise ConfigurationError(
            'ffmpeg library not found at \'%s\'.' % FFMPEG_PATH
        )

    command = [FFMPEG_PATH, '-v', 'info'] + list(args)
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    last_line = None
    analysis = {}

    def dump(data):
        if data is not None:
            interpreter.interpret_line(data)

            while any(analysis):
                analysis.pop(list(analysis.keys())[0])

    while True:
        try:
            line = proc.stdout.readline().strip()
        except Exception:  # pragma: no cover
            continue

        if 'Invalid argument' in line:
            raise AnalysisError(
                'Source file appears to be invalid, corrupt or otherwise '
                'unreadable by ffmpeg.'
            )

        if line == '' and proc.poll() is not None:
            break

        try:
            parse(line, analysis, dump)
        except AnalysisError:  # pragma: no cover
            logger.error('Error reading line from ffmpeg', exc_info=True)
            raise
        except Exception:
            logger.error('Error reading line from ffmpeg', exc_info=True)
            raise AnalysisError('Error reading line from ffmpeg')

        last_line = line
        if interpreter.finished:
            proc.terminate()
            return

    interpreter.done()
    if proc.returncode != 0:
        raise AnalysisError(last_line)

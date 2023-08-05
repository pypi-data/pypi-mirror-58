from .exceptions import FileError
from .interpretation import Interpreter
from . import ffmpeg, parsers
import os


FFMPEG_FORMAT_COMMANDS = (
    'astats=metadata=1:'
    'reset=1,ametadata=print:'
    'key=lavfi.astats.Overall.RMS_level'
)


def analyse(filename, reporter):
    if not os.path.exists(filename):
        raise FileError('Input file does not exist.')

    interpreter = Interpreter(reporter)
    ffmpeg.run(
        '-i', filename,
        '-af', FFMPEG_FORMAT_COMMANDS,
        '-f', 'null', '-',
        parser=parsers.rms,
        interpreter=interpreter
    )

    reporter.finish()

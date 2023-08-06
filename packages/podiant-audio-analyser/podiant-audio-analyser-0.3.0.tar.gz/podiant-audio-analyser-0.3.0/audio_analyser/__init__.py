from .exceptions import FileError
from .interpretation import Interpreter
from . import ffmpeg
import os


__version__ = '0.3.0'


FFMPEG_FORMAT_COMMANDS = (
    'astats=metadata=1:reset=1,'
    'ametadata=print:key=lavfi.astats.Overall.RMS_level,'
    'ebur128'
)


def analyse(filename, reporter):
    if not os.path.exists(filename):
        raise FileError('Input file does not exist.')

    interpreter = Interpreter(reporter)
    ffmpeg.run(
        '-i', filename,
        '-af', FFMPEG_FORMAT_COMMANDS,
        '-f', 'null', '-',
        interpreter=interpreter
    )

    reporter.finish()

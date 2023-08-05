"""
Audio analysis toolkit, using ffmpeg
"""
from setuptools import find_packages, setup
import os
import re

dependencies = ['Click']


def get_version(*file_paths):
    """Retrieves the version from audio_analyser/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M
    )

    if version_match:
        return version_match.group(1)

    raise RuntimeError('Unable to find version string.')


version = get_version('audio_analyser', '__init__.py')

setup(
    name='podiant-audio-analyser',
    version=version,
    url='https://git.steadman.io/podiant/podiant-audio-analyser',
    license='BSD',
    author='Mark Steadman',
    author_email='mark@steadman.io',
    description='Audio analysis toolkit, using ffmpeg',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'paa = audio_analyser.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)

"""
Audio analysis toolkit, using ffmpeg
"""
from setuptools import find_packages, setup

dependencies = ['Click']

setup(
    name='podiant-audio-analyser',
    version='0.1',
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

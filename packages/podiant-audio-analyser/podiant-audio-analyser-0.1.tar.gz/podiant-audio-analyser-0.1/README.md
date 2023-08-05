Podiant audio analyser
======================

![Build](https://git.steadman.io/podiant/podiant-audio-analyser/badges/master/build.svg)
![Coverage](https://git.steadman.io/podiant/podiant-audio-analyser/badges/master/coverage.svg)

## Developing locally

The best way to run this is with [podiant-core](https://git.steadman.io/podiant/podiant-core), as this project receives instructions via a Redis queue, and you can set all that up by running podiant-core in development mode, via `docker-compose up`.

## Running tests

To run tests in a Python virtualenv, you'll need to run the following:

```
brew install ffmpeg
pip install -r requirements-testing.txt
pip install -r requirements.txt
pytest --cov audio_analyser tests
```

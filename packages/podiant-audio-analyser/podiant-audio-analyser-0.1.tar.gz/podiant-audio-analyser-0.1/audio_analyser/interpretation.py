from logging import getLogger
from .analysis import analysers


class Interpreter(object):
    def __init__(self, reporter, done=None):
        self.offset = 0
        self.batch = []
        self.analysers = []
        self.logger = getLogger('audio_analyser')
        self.finished = False
        self.__done = done

        for Analyser in analysers:
            analyser = Analyser(reporter)
            self.logger.debug('Starting %s' % analyser.verbose_name)
            self.analysers.append(analyser)

    def interpret_line(self, data):
        delta = data['time'] - self.offset
        self.batch.append(data)

        if delta >= 1:
            self.interpret_batch(self.batch)
            self.batch = []
            self.offset = data['time']

    def interpret_batch(self, batch):
        any_remaining = False

        for analyser in self.analysers:
            if not analyser.finished:
                analyser.read_chunk(
                    int(self.offset),
                    batch
                )

                if not analyser.finished:
                    any_remaining = True

        if not any_remaining:
            self.done()

    def done(self):
        if self.finished:
            return

        self.finished = True
        self.logger.debug('Finished analysis.')

        if any(self.batch):
            self.interpret_batch(self.batch)

        for analyser in self.analysers:
            if not analyser.finished:
                self.logger.debug('Finishing %s.' % analyser.verbose_name)
                analyser.finish()

        self.logger.debug('All analysers have finished.')
        if self.__done is not None and callable(self.__done):
            self.__done()

from logging import getLogger
from .analysis import analysers
from .parsing import parsers


class Interpreter(object):
    def __init__(self, reporter, done=None):
        self.offset = 0
        self.batch = []
        self.logger = getLogger('audio_analyser')
        self.finished = False
        self.__done = done
        self.__analysers = []

        for Analyser in analysers:
            analyser = Analyser(reporter)
            self.logger.debug('Starting %s' % analyser.verbose_name)
            self.__analysers.append(analyser)

        self.__parsers = []
        self.__summary = {}

        for Parser in parsers:
            parser = Parser()
            parser.on('meter', self.interpret_rms)
            parser.on('summary', self.interpret_summary)
            self.logger.debug('Starting %s' % parser.verbose_name)
            self.__parsers.append(parser)

    def parse_line(self, line):
        for parser in self.__parsers:
            parser.parse(line)

    def interpret_summary(self, data):
        self.__summary.update(data)

    def interpret_rms(self, data):
        delta = data['time'] - self.offset
        self.batch.append(data)

        if delta >= 1:
            self.interpret_batch(self.batch)
            self.batch = []
            self.offset = data['time']

    def interpret_batch(self, batch):
        any_remaining = False

        for analyser in self.__analysers:
            if not analyser.finished:
                analyser.meter(
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

        if any(self.__summary):
            for analyser in self.__analysers:
                if not analyser.finished:
                    analyser.summarise(self.__summary)

        for analyser in self.__analysers:
            if not analyser.finished:
                self.logger.debug('Finishing %s.' % analyser.verbose_name)
                analyser.finish()

        self.logger.debug('All analysers have finished.')
        if self.__done is not None and callable(self.__done):
            self.__done()

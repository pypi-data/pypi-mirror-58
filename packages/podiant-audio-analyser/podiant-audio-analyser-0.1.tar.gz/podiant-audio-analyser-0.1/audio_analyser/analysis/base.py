from logging import getLogger


class AnalyserBase(object):
    def __init__(self, reporter):
        verbose_name = ''
        slug = ''

        name = type(self).__name__
        for letter in name:
            if not verbose_name:
                verbose_name = letter
            elif letter == letter.upper():
                verbose_name += ' ' + letter.lower()
            else:
                verbose_name += letter

        if name.endswith('Analyser'):
            name = name[:-len('Analyser')]

        for letter in name:
            if not slug:
                slug = letter.lower()
            elif letter == letter.upper():
                slug += '-' + letter.lower()
            else:
                slug += letter

        self.verbose_name = verbose_name
        self.slug = slug
        self.finished = False
        self.logger = getLogger('audio_analyser')
        self.reporter = reporter

    def read_chunk(self, offset, data):  # pragma: no cover
        raise NotImplementedError('Method not implemented')

    def report(self, **kwargs):
        data = {
            'reporter': self.slug
        }

        data.update(kwargs)
        self.reporter.report(data)

    def done(self):
        self.logger.debug('%s has finished.' % self.verbose_name)
        self.finished = True

    def finish(self):
        pass

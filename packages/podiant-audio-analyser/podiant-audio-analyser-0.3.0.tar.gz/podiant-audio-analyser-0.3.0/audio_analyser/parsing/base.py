from collections import defaultdict


class ParserBase(object):
    def __init__(self):
        self._data = {}
        self._callbacks = defaultdict(list)

        verbose_name = ''
        for letter in type(self).__name__:
            if not verbose_name:
                verbose_name = letter
            elif letter == letter.upper():
                verbose_name += ' ' + letter.lower()
            else:
                verbose_name += letter

        self.verbose_name = verbose_name

    def on(self, event, callback):
        self._callbacks[event].append(callback)

    def _emit(self, event, data):
        for callback in self._callbacks[event]:
            callback(data)

    def parse(self, line):
        raise NotImplementedError('Method not implemented')

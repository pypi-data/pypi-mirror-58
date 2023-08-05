import json
import sys


class ReporterBase(object):
    def report(self, data):  # pragma: no cover
        raise NotImplementedError('Method not implemented')

    def finish(self):
        pass


class ConsoleReporter(ReporterBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sys.stdout.write('[')
        sys.stdout.flush()
        self.reported = False

    def report(self, data):
        if self.reported:
            sys.stdout.write(',')

        json.dump(data, sys.stdout)
        self.reported = True
        sys.stdout.flush()

    def finish(self):
        sys.stdout.write(']')
        sys.stdout.flush()


class TestReporter(ReporterBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    def report(self, data):
        self.data.append(data)

from entry import Entry
from html_parser import Parse

class Message():
    def __init__(self, istream=None, system=None):
        assert system is not None, 'Abstract class!'
        self._istream = istream
        self._system = system
        self._entries = None
        if istream:
            self.parse()

    def parse(self):
        raise NotImplemented

    def entries(self):
        if self._entries is None:
            self._istream.seek(0)
            self.parse()
        return self._entries


class FooMessage(Message):
    def __init__(self, istream=None, system='foo'):
        Message.__init__(self, istream, system)

    def parse(self):
        istream = self._istream
        system = self._system

        self._entries = [
            Entry(
                system=self._system,
                function='dummy',
            ),
            Entry(
                system=self._system,
                function='dummy',
            ),
        ]


class PTPMessage(Message):
    def __init__(self, istream=None, system='ptp'):
        Message.__init__(self, istream, system)

    def parse(self):
        istream = self._istream
        system = self._system

        parser = Parse('\n'.join(istream.readlines()))
        return parser.entries()


class AthenaMessage(Message):
    def __init__(self, istream=None, system='athena'):
        Message.__init__(self, istream, system)

    def parse(self):
        istream = self._istream
        system = self._system

        # TODO: Do the parsing.
        raise NotImplemented


dictMessage = {
    'foo': FooMessage,
    'ptp': PTPMessage,
    'athena': AthenaMessage,
}

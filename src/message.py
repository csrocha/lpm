class Message():
    def __init__(self, istream=None, system=None):
        assert (system is not None, 'Abstract class!')
        self._istream = istream
        self._system = system
        self._entries = None
        if istream:
            self.parse(istream)

    def parse(self):
        raise NotImplemented

    def entries(self):
        if self._entries is None:
            self._istream.seek(0)
            self.parse(self._istream)
        return self._entries


class PTPMessage(Message):
    def __init__(self, istream=None, system='ptp'):
        super(PTPMessage, self).__init__(istream, system)

    def parse(self):
        istream = self._istream
        system = self._system

        # TODO: Do the parsing.
        raise NotImplemented


class AthenaMessage(Message):
    def __init__(self, istream=None, system='athena'):
        super(PTPMessage, self).__init__(istream, system)

    def parse(self):
        istream = self._istream
        system = self._system

        # TODO: Do the parsing.
        raise NotImplemented


dictMessage = {
    'ptp': PTPMessage,
    'athena': AthenaMessage,
}

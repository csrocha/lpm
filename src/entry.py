from datetime import datetime

class Entry:
    def __init__(self, **kargs):
        self._system = kargs.get('system')
        self._function = kargs.get('function')
        self._date = kargs.get('date', datetime.now())
        self._message = kargs.get('message')
        self._comments = kargs.get('comments')
        self._keywords = kargs.get('keywords', [])
        self._data = kargs.get('keywords', {})
        pass

    @property
    def system(self):
        return self._system

    @property
    def function(self):
        return self._function

    @property
    def date(self):
        return self._date if isinstance(self._date, datetime) else None

    @property
    def message(self):
        return self._message

    @property
    def comments(self):
        return self._comments

    @property
    def keywords(self):
        return self._keywords

    @property
    def data(self):
        return self._data

    def __str__(self):
        return "Entry { %s, %s, %s, %s, %s, %s }" % (
            self.system,
            self.function,
            self.date,
            self.message,
            self.comments,
            self.keywords,
        )


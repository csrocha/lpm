import json
import requests


class Publisher:
    def __init__(self, url, user, password):
        self._url = url
        self._user = user
        self._password = password

    def pushEntry(self, entry):
        _json = json.dumps({
            'sysmtem': entry._system,
            'function': entry._function or '',
            'date': entry._date.strftime("%a %b %d %H:%M:%S %Z %Y"),
            'message': entry._message or '',
            'comments': entry._comments or '',
            'data': json.dumps(entry._data),
            'keywords': json.dumps(entry.keywords),
        })

        response = requests.post(
            self._url,
            data=_json,
            auth=(self._user, self._password))

        return response.status_code == 201

    def pushEntries(self, entries):
        return [self.pushEntry(e) for e in entries]

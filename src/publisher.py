import json
import requests
import logging

class Publisher:
    def __init__(self, url, user, password):
        self._url = url
        self._user = user
        self._password = password

    def pushEntry(self, entry):
        _json = json.dumps({
            'sysmtem': entry.system,
            'function': entry.function or '',
            'date': entry.date.strftime("%a %b %d %H:%M:%S %Z %Y"),
            'message': entry.message or '',
            'comments': entry.comments or '',
            'data': json.dumps(entry.data),
            'keywords': json.dumps(entry.keywords),
        })

        logging.info("Publishing: %s", entry)

        response = requests.post(
            self._url,
            data=_json,
            auth=(self._user, self._password))

        return response.status_code == 201

    def pushEntries(self, entries):
        return [self.pushEntry(e) for e in entries]

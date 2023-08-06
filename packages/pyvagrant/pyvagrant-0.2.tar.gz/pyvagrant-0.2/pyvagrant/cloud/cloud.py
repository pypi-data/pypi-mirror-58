import logging
import subprocess
import json

class Cloud(object):
    def __init__(self, vagrant):
        self._vagrant = vagrant
        self._authenticated = None

    def authenticate(self, user):
        subprocess.run(["vagrant", "cloud", "auth", "login", "-u", user])
        self._authenticated = None

    def search(self, term):
        """Search for boxes with term."""

        if not self.authenticated:
            LOGGER.error("Must be authenticated to search. Please .authenticate first.")
            return

        results = subprocess.check_output(["vagrant", "cloud", "search", "-j", term])
        results = json.loads(results)

        return [
                Box(self._vagrant, result['name'], result['version'], result['downloads'], result['providers'])
                for result in results
            ]

    @property
    def authenticated(self):
        if self._authenticated is not None:
            return self._authenticated

        try:
            subprocess.check_output(["vagrant", "cloud", "auth", "login", "-c"], stderr=subprocess.PIPE)
            self._authenticated = subprocess.check_output(["vagrant", "cloud", "auth", "whoami"]).split(b"logged in as ")[1].decode().strip()

        except subprocess.CalledProcessError:
            self._authenticated = False

        return self._authenticated

from ..box import Box
LOGGER = logging.getLogger(__name__)

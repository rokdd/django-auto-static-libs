import requests

class BaseProvider:
    def download(self):
        pass

class SingleUrlProvider(BaseProvider):
    def __init__(self, url):
        self.url = url

    def download(self):
        r = requests.get(self.url,allow_redirects=True)

        # we got not a valid answer of a file:
        if not r.ok or r.content is None:
            return None

        return r

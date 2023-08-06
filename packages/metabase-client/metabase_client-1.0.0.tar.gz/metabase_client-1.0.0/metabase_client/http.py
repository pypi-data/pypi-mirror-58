from urllib.parse import urljoin

import requests


class HttpClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def authenticated(self, method, path, token, **kwargs):
        headers = {"Content-Type": "application/json", "X-Metabase-Session": token}
        return self.request(method, path, headers=headers, **kwargs)

    def request(self, method, path, **kwargs):
        url = urljoin(self.endpoint, path)
        return requests.request(method, url, **kwargs)

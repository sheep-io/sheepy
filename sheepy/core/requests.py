import requests
from ..utils.httperror import HttpError

class ApiRequests:
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method, endpoint, **kwargs):
        response = requests.request(method, f"{self.base_url}{endpoint}", **kwargs)
        self._handle_response(response)
        return response

    def get(self, endpoint, params=None):
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint, json=None):
        return self.request("POST", endpoint, json=json)

    def put(self, endpoint, json=None):
        return self.request("PUT", endpoint, json=json)

    def delete(self, endpoint):
        return self.request("DELETE", endpoint)

    def _handle_response(self, response):
        if not response.ok:
            raise HttpError(response.status_code, response.text)

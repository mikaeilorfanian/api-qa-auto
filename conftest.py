from dataclasses import dataclass
import os

from pytest import fixture
import requests


BASE_URL = os.environ.get('BASE_API_URL', 'https://jsonplaceholder.typicode.com')


@dataclass
class HttpClient:
    base_url: str
    session: requests.Session = None

    def __post_init__(self):
        self.session = requests.Session()

    def post(self, path: str, payload: dict):
        return self.session.post(url=self._full_url(path), data=payload)

    def get(self, path: str, payload: dict = None):
        if payload:
            return self.session.get(url=self._full_url(path), data=payload)

        return self.session.get(url=self._full_url(path))

    def put(self, path: str, payload: dict):
        return self.session.put(url=self._full_url(path), data=payload)

    def patch(self, path: str, payload: dict):
        return self.session.patch(url=self._full_url(path), data=payload)

    def _full_url(self, path: str):
        return self.base_url + path


@fixture(scope='session')
def http_client():
    return HttpClient(base_url=BASE_URL)


@fixture
def post_object():
    return {'title': 'foo', 'body': 'bar', 'userId': 1}

import requests
from lib.base_case import BaseCase

class TestHomeworkCookie(BaseCase):
    def test_header(self):
        response1 = requests.get('https://playground.learnqa.ru/api/homework_header')
        self.header = self.get_headers(response1, "x-secret-homework-header")
        assert self.header == "Some secret value", f"Header have a wrong value - '{self.header}'"
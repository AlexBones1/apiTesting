import requests
from lib.base_case import BaseCase

class TestHomeworkCookie(BaseCase):
    def test_cookie(self):
        response1 = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        self.cookie = self.get_cookie(response1, "HomeWork")
        assert self.cookie == "hw_value", f"Cookie have wrong value - '{self.cookie}'"
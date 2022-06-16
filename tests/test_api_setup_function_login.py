import pytest
import requests
from lib.base_case import BaseCase

class TestUserAuth(BaseCase):
    exclude_params = [
        ("no cookie"),
        ("no_token")
    ]

    def setup(self):
        payload = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=payload)
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_headers(response1, "x-csrf-token")
        self.user_id_from_auth = self.get_json_value(response1, "user_id")

    def test_user_auth(self):
        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )

        self.user_id_from_check_method = self.get_json_value(response2, "user_id")
        assert self.user_id_from_auth == self.user_id_from_check_method, "user_id's is not equal"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_check(self, condition):
        if condition == "no cookie":
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={"x-csrf-token": self.token}
            )

        else:
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={"auth_sid": self.auth_sid}
            )
        assert "user_id" in response2.json(), "There is no user_id in the second response"

        self.user_id_from_check_method = self.get_json_value(response2, "user_id")
        assert self.user_id_from_check_method == 0, f"User is authorized with condition {condition}"

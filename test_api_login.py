import pytest
import requests


class TestUserAuth:
    def test_user_auth(self):
        payload = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=payload)

        assert "auth_sid" in response1.cookies, "there is no auth cookies in response"
        assert "x-csrf-token" in response1.headers, "there is no csrf token in response"
        assert "user_id" in response1.json(), "there is no user_id in response"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth = response1.json()["user_id"]

        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        assert "user_id" in response2.json(), "there is no user_id in second response"

        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_auth == user_id_from_check_method, "user_id's is not equal"

    exclude_params = [
        ("no cookie"),
        ("no_token")
    ]
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_check(self, condition):
        payload = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=payload)

        assert "auth_sid" in response1.cookies, "there is no auth cookies in response"
        assert "x-csrf-token" in response1.headers, "there is no csrf token in response"
        assert "user_id" in response1.json(), "there is no user_id in response"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")

        if condition == "no cookie":
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={"x-csrf-token": token}
            )

        else:
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={"auth_sid": auth_sid}
            )
        assert "user_id" in response2.json(), "There is no user_id in the second response"

        user_id_from_check_method = response2.json()["user_id"]
        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"
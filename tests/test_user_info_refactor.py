from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserInfo(BaseCase):
    def test_user_info_not_auth(self):
        response = MyRequests.get("/user/1")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_no_key(response, "email")
        Assertions.assert_json_has_no_key(response, "firstName")
        Assertions.assert_json_has_no_key(response, "lastName")

    def test_get_user_info_auth_as_same_user(self):
        payload = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = MyRequests.post('/user/login', data=payload)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_headers(response1, "x-csrf-token")
        user_id_auth = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{user_id_auth}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        expected_fields = [
            "username",
            "email",
            "firstName",
            "lastName"
        ]
        Assertions.assert_json_has_keys(response2, expected_fields)

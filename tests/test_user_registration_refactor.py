from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    def test_create_new_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_status_code(response, 200)

    def test_create_user_with_existed_email(self):
        email = 'testov@test.ru'
        data = self.prepare_registration_data(email)

        response = MyRequests.post('/user/', data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",\
            f"Unexpected response content {response.content.decode('utf-8')}"

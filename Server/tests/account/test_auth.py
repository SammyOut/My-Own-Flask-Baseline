from tests import TCBase, check_status_code
from tests.requests import signup_request, auth_request


class AuthTest(TCBase):

    def setUp(self):
        super(AuthTest, self).setUp()
        signup_request(self)

    @check_status_code(204)
    def test_wrong_id(self):
        return auth_request(self, id='123456')

    @check_status_code(204)
    def test_wrong_password(self):
        return auth_request(self, password='1234567890')

    @check_status_code(200)
    def test_success(self):
        return auth_request(self)

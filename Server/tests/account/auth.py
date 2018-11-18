from json import dumps

from tests import TCBase, check_status_code


class AuthTest(TCBase):

    def setUp(self):
        super(AuthTest, self).setUp()
        self.create_account()

    def auth_request(self, id='12345', password='12345678'):
        return self.client.post(
            '/auth',
            data=dumps(
                dict(id=id, password=password)
            ),
            content_type='application/json'
        )

    @check_status_code(204)
    def test_wront_id(self):
        return self.auth_request(id='123456')

    @check_status_code(204)
    def test_wrong_password(self):
        return self.auth_request(password='1234567890')

    @check_status_code(200)
    def test_success(self):
        return self.auth_request()

from json import dumps

from tests import TCBase


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

    def _success_signup(self, rv):
        self.assertEqual(rv.status_code, 200)

    def _fail_signup(self, rv):
        self.assertEqual(rv.status_code, 204)

    def test_wront_id(self):
        rv = self.auth_request(id='123456')
        self._fail_signup(rv)

    def test_wrong_password(self):
        rv = self.auth_request(password='1234567890')
        self._fail_signup(rv)

    def test_success(self):
        rv = self.auth_request()
        self._success_signup(rv)

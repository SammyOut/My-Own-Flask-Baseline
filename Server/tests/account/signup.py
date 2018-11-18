from json import dumps

from tests import TCBase


class SignupTest(TCBase):

    def signup_request(self, id_='12345', password='12345678', email='python@istruly.sexy'):
        return self.client.post(
            '/signup',
            data=dumps(
                dict(id=id_, password=password, email=email)
            ),
            content_type='application/json'
        )

    def _success_signup(self, rv):
        self.assertEqual(rv.status_code, 201)

    def _fail_signup(self, rv):
        self.assertEqual(rv.status_code, 205)

    def test_wrong_id_length(self):
        rv = self.signup_request(id_='1234')
        self._fail_signup(rv)

        rv = self.signup_request(id_='123456789012345678901')
        self._fail_signup(rv)

    def test_wrong_password_length(self):
        rv = self.signup_request(password='1234567')
        self._fail_signup(rv)

        rv = self.signup_request(password='123456789012345678901234567890123')
        self._fail_signup(rv)

    def test_wrong_email_format(self):
        rv = self.signup_request(email='aaa@dsdf')
        self._fail_signup(rv)

        rv = self.signup_request(email='aaadsdf,dsf')
        self._fail_signup(rv)

    def test_exist_id(self):
        self.signup_request()

        rv = self.signup_request(password='1234567890', email='aa@aaa.aa')
        self._fail_signup(rv)

    def test_success(self):
        rv = self.signup_request()
        self._success_signup(rv)

        rv = self.signup_request(id_='12345678901234567890', password='12345678901234567890123456789012', email='aa@aa.aa')
        self._success_signup(rv)

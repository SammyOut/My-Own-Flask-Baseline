from json import dumps

from tests import TCBase, check_status_code


class SignupTest(TCBase):

    def signup_request(self, id_='12345', password='12345678', email='python@istruly.sexy'):
        return self.client.post(
            '/signup',
            data=dumps(
                dict(id=id_, password=password, email=email)
            ),
            content_type='application/json'
        )

    @check_status_code(205)
    def test_short_id_length(self):
        return self.signup_request(id_='1234')

    @check_status_code(205)
    def test_long_id_length(self):
        return self.signup_request(id_='123456789012345678901')

    @check_status_code(205)
    def test_short_password_length(self):
        return self.signup_request(password='1234567')

    @check_status_code(205)
    def test_long_password_length(self):
        return self.signup_request(password='123456789012345678901234567890123')

    @check_status_code(205)
    def test_no_dot_email(self):
        return self.signup_request(email='aaa@dsdf')

    @check_status_code(205)
    def test_no_at_email(self):
        return self.signup_request(email='aaadsdf.dsf')

    @check_status_code(205)
    def test_exist_id(self):
        self.signup_request()
        return self.signup_request(password='1234567890', email='aa@aaa.aa')

    @check_status_code(201)
    def test_success_min_length_id_password(self):
        return self.signup_request()

    @check_status_code(201)
    def test_success_max_length_id_password(self):
        return self.signup_request(id_='12345678901234567890', password='12345678901234567890123456789012', email='aa@aa.aa')

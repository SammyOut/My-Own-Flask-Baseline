from tests import TCBase, check_status_code
from tests.requests import signup_request


class SignupTest(TCBase):

    @check_status_code(205)
    def test_short_id_length(self):
        return signup_request(self, id_='1234')

    @check_status_code(205)
    def test_long_id_length(self):
        return signup_request(self, id_='123456789012345678901')

    @check_status_code(205)
    def test_short_password_length(self):
        return signup_request(self, password='1234567')

    @check_status_code(205)
    def test_long_password_length(self):
        return signup_request(self, password='123456789012345678901234567890123')

    @check_status_code(205)
    def test_no_dot_email(self):
        return signup_request(self, email='aaa@dsdf')

    @check_status_code(205)
    def test_no_at_email(self):
        return signup_request(self, email='aaadsdf.dsf')

    @check_status_code(205)
    def test_exist_id(self):
        signup_request(self)
        return signup_request(self, password='1234567890', email='aa@aaa.aa')

    @check_status_code(201)
    def test_success_min_length_id_password(self):
        return signup_request(self)

    @check_status_code(201)
    def test_success_max_length_id_password(self):
        return signup_request(self, id_='12345678901234567890', password='12345678901234567890123456789012', email='aa@aa.aa')

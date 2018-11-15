from json import dumps

from tests import TCBase


class SignupTest(TCBase):

    def signup_request(self, id='Nerd-Bear', password='Nerd-Bear', email='python@istruly.sexy'):
        return self.client.post(
            '/signup',
            data=dumps(
                dict(id=id, password=password, email=email)
            )
        )

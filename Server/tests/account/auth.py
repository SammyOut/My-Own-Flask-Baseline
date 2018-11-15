from json import dumps

from tests import TCBase


class AuthTest(TCBase):

    def auth_request(self, id='Nerd-Bear', password='Nerd-Bear'):
        return self.client.post(
            '/auth',
            data=dumps(
                dict(id=id, password=password)
            )
        )

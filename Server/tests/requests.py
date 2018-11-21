from json import dumps


def signup_request(self, id_='12345', password='12345678', email='python@istruly.sexy'):
    return self.client.post(
        '/signup',
        data=dumps(
            dict(id=id_, password=password, email=email)
        ),
        content_type='application/json'
    )


def auth_request(self, id='12345', password='12345678'):
    return self.client.post(
        '/auth',
        data=dumps(
            dict(id=id, password=password)
        ),
        content_type='application/json'
    )

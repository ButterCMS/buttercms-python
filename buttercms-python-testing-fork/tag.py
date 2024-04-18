from .client import Client


class Tag(Client):
    """Tag"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'tags/'

    def all(self, params=None):
        return self.api_get(params=params)

from .client import Client


class Author(Client):
    """Author"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'authors/'

    def all(self, params=None):
        return self.api_get(params=params)

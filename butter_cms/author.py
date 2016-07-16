from client import Client


class Author(Client):
    """Author"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'authors/'

    def all(self, include=None):
        params = {'include': include} if include else {}
        return self.api_get(params=params)

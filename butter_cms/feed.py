from client import Client


class Feed(Client):
    """Feed"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'feeds/'

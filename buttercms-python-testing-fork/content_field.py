from .client import Client


class ContentField(Client):
    """ContentField"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'content/'

    def get(self, keys=None, params=None):
        if not params:
            params = {}
        params['keys'] = ','.join(keys)
        return self.api_get(params=params)

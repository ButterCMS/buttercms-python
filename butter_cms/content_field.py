from .client import Client


class ContentField(Client):
    """ContentField"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'content/'

    def get(self, keys, params=None):
        if not params:
            params = {}
        params['keys'] = ','.join(keys)
        return self.api_get(params=params)
    
    def get_collection(self, slug, fields=None, params=None):
        if not params:
            params = {}
        if fields:
            for field_dict in fields:
                for key, value in field_dict.items():
                    param_key = f"fields.{key}"
                    params[param_key] = value

        full_slug = f'{slug}/'

        return self.api_get(slug=full_slug, params=params)

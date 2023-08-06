from queen.lib.api import BaseRestClient


class AnsibleTowerClient(BaseRestClient):

    @classmethod
    def fromansibleparams(cls, params, *args, **kwargs):
        client = cls(
            AnsibleTowerClient.envdefault(params, 'api_url', 'AWX_URL'),
            AnsibleTowerClient.envdefault(params, 'validate_certs', 'AWX_VALIDATE_CERTS'),
        )
        return client.basic_auth(
            AnsibleTowerClient.envdefault(params, 'api_user', 'AWX_USER'),
            AnsibleTowerClient.envdefault(params, 'api_password', 'AWX_PASSWORD'),
        )

    def collection_from_envelope(self, response, envelope):
        return envelope['results']\
            if bool(envelope.get('count'))\
            else []

    def detail_from_envelope(self, request, envelope):
        if not set(['count', 'results']) <= set(envelope.keys()):
            return envelope
        if envelope['count'] == 0:
            raise self.ResourceDoesNotExist
        elif envelope['count'] > 1:
            raise self.MultipleObjectsReturned
        return envelope['results'][0]

    def get_organization(self, **params):
        return self._get_object('organizations', **params)

    def get_credential(self, **params):
        return self._get_object('credentials', **params)

    def get_credential_type(self, **params):
        return self._get_object('credential_types', **params)

    def get_inventory(self, **params):
        return self._get_object('inventories', **params)

    def get_project(self, **params):
        return self._get_object('projects', **params)

    def get_user(self, **params):
        return self._get_object('users', **params)

    def _get_object(self, _kind, **params):
        if not params:
            return None
        dto = self.detail(_kind, params=params)
        return dto['id']

    def asfilter(self, attname, params):
        """Returns the parameters formatted for used as a filter
        in a list lookup.
        """
        return flatten(attname, params)


def flatten(attname, params):
    new_params = {}
    for k,v in dict.items(params):
        key = f'{attname}__{k}' if attname else k
        if not isinstance(v, dict):
            new_params[key] = v
            continue
        for x, y in dict.items(flatten(key, v)):
            new_params[x] = y
    return new_params

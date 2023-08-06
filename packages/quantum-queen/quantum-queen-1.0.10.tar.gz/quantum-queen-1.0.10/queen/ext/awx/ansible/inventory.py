from .base import BaseAnsibleTowerModule


class InventoryModule(BaseAnsibleTowerModule):
    module_args = {
        'api_url': {'type': 'str', 'required': False},
        'api_user': {'type': 'str', 'required': False},
        'api_password': {'type': 'str', 'required': False, 'no_log': True},
        'validate_certs': {'type': 'bool', 'required': False, 'default': False},
        'state': {'type': 'str', 'required': False, 'default': 'present'},
        'organization': {'type': 'dict', 'required': True},
        'kind': {'type': 'str', 'required': False, 'default': ""},
        'name': {'type': 'str', 'required': True},
        'description': {'type': 'str', 'required': False, 'default': ""},
        'variables': {'type': 'str', 'required': False, 'default': ""},
    }

    def getsubjectresource(self):
        params = {'name': self.params['name']}
        params.update(self.client.asfilter(
            'organization', self.params['organization']))
        return self.client.list('inventories', params=params)

    def dtofromparams(self):
        return {
            'organization': self.client.get_organization(**self.params['organization']),
            'name': self.params['name'],
            'description': str.strip(self.params['description']),
            'variables': self.params['variables'],
        }

    def getcreateurlparts(self):
        return ['POST', 'inventories']

    def getupdateurlparts(self):
        return ['PUT', 'inventories', self.resource['id']]

    def getdeleteurlparts(self):
        return ['DELETE', 'inventories', self.resource['id']]

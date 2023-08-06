from .base import BaseAnsibleTowerModule


class CredentialModule(BaseAnsibleTowerModule):
    module_args = {
        'api_url': {'type': 'str', 'required': False},
        'api_user': {'type': 'str', 'required': False},
        'api_password': {'type': 'str', 'required': False, 'no_log': True},
        'validate_certs': {'type': 'bool', 'required': False, 'default': False},
        'state': {'type': 'str', 'required': False, 'default': 'present'},
        'credential_type': {'type': 'dict', 'required': False, 'default': {}},
        'organization_id': {'type': 'int', 'required': False},
        'organization': {'type': 'dict', 'required': False, 'default': {}},
        'name': {'type': 'str', 'required': True},
        'kind': {'type': 'str', 'required': False},
        'description': {'type': 'str', 'required': False},
        'inputs': {'type': 'dict', 'required': False},
    }

    def getsubjectresource(self):
        params={'name': self.params['name']}
        if params.get('organization_id'):
            params['organization_id'] = self.params['organization_id']
        if self.params.get('credential_type'):
            if 'id' in self.params['credential_type']:
                params['credential_type__id'] = self.params['credential_type']['id']
            else:
                params['credential_type__kind'] = self.params['credential_type']['kind']
                params['credential_type__name'] = self.params['credential_type']['name']
        if self.params.get('organization'):
            params.update(self.client.asfilter('organization', self.params['organization']))
        return self.client.list('credentials', params=params)

    def dtofromparams(self):
        dto = {
            'credential_type': self.client.get_credential_type(**self.params['credential_type']),
            'name': self.params['name'],
            'description': str.strip(self.params['description']),
            'inputs': self.params['inputs'],
        }
        if not set(['user', 'team', 'organization']) & set(self.params.keys()):
            dto['user'] = self.client.get_user(username=self.params['api_user'])
        elif 'organization' in self.params:
            dto['organization'] = self.client.get_organization(**self.params['organization'])
        else:
            raise NotImplementedError
        return dto

    def getcreateurlparts(self):
        return ['POST', 'credentials']

    def getupdateurlparts(self):
        return ['PUT', 'credentials', self.resource['id']]

    def getdeleteurlparts(self):
        return ['DELETE', 'credentials', self.resource['id']]

    def run(self):
        if not self.isremoved():
            if not self.facts_only() and not self.params.get('inputs'):
                self.fail("The `inputs` parameter is required.")
            if not self.facts_only() and not self.params.get('credential_type'):
                self.fail("The `credential_type` parameter is required.")
            if not self.facts_only() and not self.params.get('description'):
                self.fail("The `description` parameter is required.")
        return super().run()


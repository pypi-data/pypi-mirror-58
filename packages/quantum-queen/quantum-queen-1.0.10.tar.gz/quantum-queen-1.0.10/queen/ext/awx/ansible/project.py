from .base import BaseAnsibleTowerModule


class ProjectModule(BaseAnsibleTowerModule):
    module_args = {
        'api_url': {'type': 'str', 'required': False},
        'api_user': {'type': 'str', 'required': False},
        'api_password': {'type': 'str', 'required': False, 'no_log': True},
        'validate_certs': {'type': 'bool', 'required': False, 'default': False},
        'state': {'type': 'str', 'required': False, 'default': 'present'},
        'organization': {'type': 'dict', 'required': True},
        'name': {'type': 'str', 'required': True},
        'description': {'type': 'str', 'required': False, 'default': ""},
        'credential': {'type': 'dict', 'required': False, 'default': {}},
        'scm_type': {'type': 'str', 'required': False},
        'scm_url': {'type': 'str', 'required': False},
        'scm_branch': {'type': 'str', 'default': 'master'},
        'scm_delete_on_update': {'type': 'bool', 'required': False, 'default': False},
        'scm_clean': {'type': 'bool', 'required': False, 'default': False},
        'scm_update_on_launch': {'type': 'bool', 'required': False, 'default': False},
        'scm_update_cache_timeout': {'type': 'int', 'required': False, 'default': 0},
    }

    def getsubjectresource(self):
        params = {'name': self.params['name']}
        params.update(self.client.asfilter(
            'organization', self.params['organization']))
        return self.client.list('projects', params=params)

    def dtofromparams(self):
        if not self.params.get('scm_branch'):
            self.fail("The scm_branch parameter is required.")
        if not self.params.get('scm_type'):
            self.fail("The scm_type parameter is required.")
        return {
            'organization': self.client.get_organization(**self.params['organization']),
            'credential': self.client.get_credential(**self.params['credential']),
            'name': self.params['name'],
            'description': str.strip(self.params['description']),
            'scm_type': self.params['scm_type'],
            'scm_url': self.params['scm_url'],
            'scm_branch': self.params['scm_branch'],
            'scm_delete_on_update': self.params['scm_delete_on_update'],
            'scm_clean': self.params['scm_clean'],
            'scm_update_on_launch': self.params['scm_update_on_launch'],
            'scm_update_cache_timeout': self.params['scm_update_cache_timeout'],
        }

    def getcreateurlparts(self):
        return ['POST', 'projects']

    def getupdateurlparts(self):
        return ['PUT', 'projects', self.resource['id']]

    def getdeleteurlparts(self):
        return ['DELETE', 'projects', self.resource['id']]

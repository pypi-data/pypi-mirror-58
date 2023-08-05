# -*- coding: utf-8 -*-

import urllib
from activewatch import NoValue
from activewatch.session import AuthenticationException
from activewatch.session import Session
from activewatch.service import Service

"""
    alertlogic.services.credentials
    ~~~~~~~~~~~~~~
    alertlogic credentials service client
"""

class Credentials(Service):
    # https://console.account.alertlogic.com/users/api/credentials/#
    def __init__(self, session, version=None, account_id = None):
        Service.__init__(self, "credentials", version if version != None else "v2", session)

    """
    V1 APIs
    """
    # /credentials/v1/:account_id/:environment_id/:asset_type/scan/:credential_type/:asset_key
    # def delete_asset_scan_credential(deployment_id, credential_type, asset_key, asset_type=None, account_id=None):


    """
    V2 APIs
    """
    # /credentials/v2/:account_id/credentials
    def create_credential(self, name, secrets, account_id=None):
        return self.post(account_id=account_id,
                        path_parts = ['credentials'],
                        json_data = {
                            'name': name,
                            'secrets': secrets
                        })

    # /credentials/v2/:account_id/credentials/:credential_id
    def delete_credential(self, credential_id, account_id=None):
        return self.delete(account_id=account_id, path_parts = ['credentials', credential_id])

    # /credentials/v2/:account_id/credentials/:credential_id
    def get_credential(self, credential_id, account_id=None):
        return self.get(account_id=account_id, path_parts = ['credentials', credential_id])

    # /credentials/v2/:account_id/credentials/:credential_id/decrypted
    def get_decrypted_credential(self, credential_id, account_id=None):
        return self.get(account_id=account_id, path_parts = ['credentials', credential_id, 'decrypted'])

    # /credentials/v2/:account_id/credentials
    def list_credentials(self, account_id=None):
        return self.get(account_id=account_id, path_parts = ['credentials'])

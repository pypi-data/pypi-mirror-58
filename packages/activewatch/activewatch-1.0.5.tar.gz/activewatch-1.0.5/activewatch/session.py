# -*- coding: utf-8 -*-

"""
    activewatch.session
    ~~~~~~~~~~~~~~
    activewatch authentication/authorization
"""
import requests
import activewatch
from activewatch.config import Config
from activewatch.region import Region


class AuthenticationException(Exception):
    def __init__(self, message):
        super(AuthenticationException, self).__init__("authentication error: {}".format(message))


class Session():
    """
    Authenticates against Alert Logic ActiveWatchaims service and stores session information (token and account id),
    additionally objects of this class can be used as auth modules for the requests lib, more info:
    http://docs.python-requests.org/en/master/user/authentication/#new-forms-of-authentication
    """

    def __init__(self, access_key_id=None, secret_key=None, aims_token=None,
            account_id=None, profile=None, global_endpoint = "production", residency="us"):
        """
        :param region: a Region object
        :param access_key_id: your Alert Logic ActiveWatchaccess_key_id or username
        :param secret_key: your Alert Logic ActiveWatchsecret_key or password
        :param aims_token: aims_token to be used for authentication. If aims_token is specified, access_key_id and secret_key paramters are ignored
        : param account_id: Alert Logic Account ID to initialize a session for. Unless account_id is provided explicitly during service connection initialization, this account id is used. If this parameter isn't specified, the account id of the access_key_id is used.
        :param: profile: name of the profile section of the configuration file
        :param: global_endpoint: Name of the global endpoint. 'production' or 'integration' are the only valid values
        :param residency: Data residency name to perform data residency dependend actions. Currently, 'default', 'us' and 'emea' are the only valid entries
        """
        
        self._config = Config(access_key_id=access_key_id, secret_key=secret_key, account_id=account_id,
                                profile=profile, global_endpoint=global_endpoint, residency=residency)

        self._account_id = self._config.account_id
        self._residency = self._config.residency
        self._global_endpoint = self._config.global_endpoint
        self._global_endpoint_url = Region.get_global_endpoint(self._global_endpoint)

        if aims_token:
            self._token = aims_token
        else:
            self._access_key_id, self._secret_key = self._config.get_auth()
            self._authenticate()

    def _set_credentials(self, access_key_id, secret_key, aims_token):
        self._access_key_id = access_key_id
        self._secret_key = secret_key
        self._token = aims_token

    def _authenticate(self):
        """
        Authenticates against alertlogic ActiveWatch Access and Identity Management Service (AIMS)
        more info:
        https://console.cloudinsight.alertlogic.com/api/aims/#api-AIMS_Authentication_and_Authorization_Resources-Authenticate
        """
        try:
            auth = requests.auth.HTTPBasicAuth(self._access_key_id, self._secret_key)
            print("Path: {}/aims/v1/authenticate".format(self._global_endpoint_url))
            response = requests.post(self._global_endpoint_url + "/aims/v1/authenticate", auth=auth)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise AuthenticationException("invalid http response {}".format(e))

        try:
            self._token = response.json()["authentication"]["token"]
        except (KeyError, TypeError, ValueError):
            raise AuthenticationException("token not found in response")

        if self._account_id is None:
            try:
                self._account_id = response.json()["authentication"]["account"]["id"]
            except (KeyError, TypeError, ValueError):
                raise AuthenticationException("account id not found in response")

        try:
            self._account_name = response.json()["authentication"]["account"]["name"]
        except (KeyError, TypeError, ValueError):
            raise AuthenticationException("account name not found in response")
        
    def __call__(self, r):
        """
        requests lib auth module callback
        """
        r.headers["x-aims-auth-token"] = self._token
        return r

    def client(self, service_name, *args, **kwargs):
        return activewatch.client(service_name, self, *args, **kwargs)

    def get_url(self, service_name, account_id = None):
        try:
            response = requests.get(
                Region.get_endpoint_url(self._global_endpoint_url,
                                        service_name,
                                        account_id or self.account_id,
                                        self.residency)
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise AuthenticationException("invalid http response from endpoints service {}".format(e))
        return "https://{}".format(response.json()[service_name])

    def request(self, method, url, params={}, headers={}, cookies={}, **kwargs):
        headers.update({'x-aims-auth-token': self._token})
        return requests.request(method, url, params=params, headers=headers, cookies=cookies, **kwargs)

    def get_defaults(self):
        return {
            "account_id": self.account_id
        }

    @property
    def account_id(self):
        return self._account_id

    @property
    def residency(self):
        return self._residency

    @property
    def account_name(self):
        return self._account_name

    @property
    def global_endpoint(self):
        return self._global_endpoint

    @property
    def global_endpoint_url(self):
        return self._global_endpoint_url

# activewatch.client.connect(session, 'deployments', cid=1234)

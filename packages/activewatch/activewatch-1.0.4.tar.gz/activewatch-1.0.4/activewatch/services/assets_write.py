# -*- coding: utf-8 -*-

import urllib
from activewatch import NoValue
from activewatch.session import AuthenticationException
from activewatch.session import Session
from activewatch.service import Service

"""
    alertlogic.services.aims
    ~~~~~~~~~~~~~~
    alertlogic assets_write service client
"""

class InvalidRequest(Exception):
    pass

class InvalidParameter(InvalidRequest):
    def __init__(self, function_name, parameter_name, problem):
        super(InvalidParameter, self).__init__("Function '{}' was given an invalid '{}' argument. {}".format(function_name, parameter_name, problem))

class Assets_write(Service):
    # https://console.account.alertlogic.com/users/api/assets_write
    def __init__(self, session, version=None, account_id = None):
        Service.__init__(self, "assets_write", version if version != None else "v1", session)

    '''
    https://console.account.alertlogic.com/users/api/assets_write/#api-Declare-CreateNetwork
    properties example
    {
        "network_name": "MyNetwork",
        "cidr_ranges": ["10.0.0.0/16"],
        "public_cidr_ranges": ["10.0.0.0/16"],
    }
    '''

    def create_network(self, deployment_id, scope, properties, account_id=None):
        if scope != 'datacenter':
            raise InvalidParameter("create_network", "scope", "currently 'datacenter' is the only valid value")

        json_data = {
            'operation': 'create_network',
            'scope': scope,
            'properties': properties
        }
        return self._put(account_id, deployment_id, json_data)

    '''    
    https://console.account.alertlogic.com/users/api/assets_write/#api-Declare-DeclareApplications
    Example
        type = "host"
        key = "/aws/us-east-1/host/i-11112222"
        destinations = [
            ["nginx", {"port": 80, "ip_protocol": "tcp"}],
            ["telnet", {"port": 992, "ip_protocol": "udp"}
        ]
    declare_applications(deployment_id, 'aws', type, key, destinations)
    '''
    def declare_applications(self, deployment_id, scope, type, key, destinations, account_id=None):
        json_data = {
            'operation': 'declare_applications',
            'scope': scope,
            'type': type,
            'key': key,
            'destinations': destinations
        }
        return self._put(account_id, deployment_id, json_data)

    '''
    https://console.account.alertlogic.com/users/api/assets_write/#api-Declare-DeclareEnvironments

    Example:
        environment_id = "9E45B6F4-D8FE-11E7-899D-E382346B56A1"
        environment_type = "azure"
        properties = {
            "environment_id": "029faa42-36f9-1005-91c0-6c400890c2a6"
        }
        declare_environment(deployment_id, 'azure' environment_id, environment_type, properties)

    '''
    def declare_environment(self, deployment_id, scope, environment_id, environment_type, properties, account_id=None):
        json_data = {
            'operation': 'declare_environment',
            'scope': scope,
            'environment_id': environment_id,
            'environment_type': environment_type,
            'properties': properties
        }
        return self._put(account_id, deployment_id, json_data)

    '''    
    https://console.account.alertlogic.com/users/api/assets_write/#api-Declare-DeclareVulnerabilities
    Example
        type = "host"
        key = "/aws/us-east-1/host/i-11112222"
    declare_vulnerabilities(deployment_id, 'aws', type, key, vulnerabilities)
    '''
    def declare_vulnerabilities(self, deployment_id, scope, type, key, vulnerabilities, account_id=None):
        json_data = {
            'operation': 'declare_vulnerabilities',
            'scope': scope,
            'type': type,
            'key': key,
            'vulnerabilities': vulnerabilities 
        }
        return self._put(account_id, deployment_id, json_data)


    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-AccumulateStatistics
        :type type: string
        :param type: The type of the asset being modified. It must be either 'agent' or 'appliance'.
        :type key: string
        :param key: The opaque, unique key for this asset, such as "/aws/us-east-1/host/i-1234567". The key and type parameters form a unique identifier for any asset.
        :type strategy: string
        :param strategy: This parameter is used by the accumulate operation. Based on this paramenter, the "accumulate" operation will increment the current calendar hour counter, shift hours when the next hour is reached, etc. Currently, only 'hourly' is supported.
        :type properties: dict
        :parm properties: A JSON Object with properties pertaining to the asset being modified. For the accumulate operation, this has to be declared and statistics must be present.

    Example
        type: "agent",
        key: "/agent/D298CD7C-CEF2-4931-A422-D12D85362340",
        strategy: "hourly",
        properties: {
             "metric_name": 1000
        }
        accumulate(deployment_id, type=type, key=key, properties=properties)

    '''
    def accumulate_statistics(self, deployment_id, type, key, properties, strategy='hourly', account_id=None):
        json_data = {
            'operation': 'accumulate',
            'scope': 'stats',
            'type': type,
            'key': key,
            'strategy': strategy,
            'properties': properties
        }
        return self._put(account_id, deployment_id, json_data)
            
    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-DeclareAccessLevels
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type asset: dict
        :param asset: This field should be an object containing the type and key of the source asset for the access levels you wish to declare.
        :type access_levels: list
        :param access_levels: A list of objects representing the access levels. Each object must have derives_from (list of objects) and destination (object), each with type and key, as well as a properties dict that must contain an access_type property. Currently access_type can only be set to "admin"
    '''
    def declare_access_levels(self, deployment_id, scope, asset, access_levels, account_id=None):
        json_data = {
            'operation': 'declare_access_levels',
            'scope': scope,
            'asset': asset,
            'access_levels': access_levels
        }
        return self._put(account_id, deployment_id, json_data)

    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-DeclareAsset     
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type type: string
        :param type: The type of the asset being created.
        :type properties: dict
        :param properties: An object whose properties pertain to the asset being created or modified.
        :type relationships: list
        :param relationships:  list of objects describing relationships to other assets. Each object in this list must have a "type" field and a "key" describing the type and key of asset the new or update asset will have a relationship to. The object may also have a "relationship_type" field indicating the type of relationship to declare.
        :type exclusive: string
        :param exclusive: This parameter can be used when the "relationships" parameter is used. When this parameter is set to "scope", it will replace all relationships of the specified scope with those provided. When it's set to "type", it will replace all relationships of the specified type(s) and scope with those provided. When it's set to "complete", it will replace all relationships with those provided. If the exclusive parameter is omitted, all relationships provided will be added to the asset.
    '''
    def declare_asset(self, deployment_id, scope, type, key, properties=None, relationships=None, exclusive=None, account_id=None):
        json_data = {
            'operation': 'declare_asset',
            'scope': scope,
            'type': type,
            'key': key,
            'properties': properties,
            'relationships': relationships
        }
        properties and json_data.update({'properties': properties})
        relationships and json_data.update({'relationships': relationships})
        exclusive and json_data.update({'exclusive': exclusive})
        return self._put(account_id, deployment_id, json_data)

    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-DeclareProperties
        :type type: string
        :param type: The type of the asset being created.
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type: key: string
        :param key: The opaque, unique key for this asset, such as "/aws/us-east-1/host/i-1234567". The key and type parameters form a unique identifier for any asset.
        :type properties: dict 
        :param properties: [Optional] An object whose properties pertain to the asset being created or modified.
        :type conditions: list
        :param conditions: [Optional] A list of conditions evaluated against the asset being modified.
        :type create: boolean
        :param create: [Optional] A flag that determines if an asset should be created by the operation, if it does not already exist.
    '''
    def declare_properties(self, deployment_id, scope, type, key, properties=None, conditions=None, create=True, account_id=None):
        json_data = {
            'operation': 'declare_properties',
            'scope': scope,
            'type': type,
            'key': key,
            'create': create
        }
        properties and json_data.update({'properties': properties})
        conditions and json_data.update({'conditions': conditions})
        return self._put(account_id, deployment_id, json_data)

    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-DeclareRelationships
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type type: string
        :param type: The type of the asset being created.
        :type relationships: list
        :param relationships:  list of objects describing relationships to other assets. Each object in this list must have a "type" field and a "key" describing the type and key of asset the new or update asset will have a relationship to. The object may also have a "relationship_type" field indicating the type of relationship to declare.
    '''
    def declare_relationships(self, deployment_id, scope, type, key, relationships=None, account_id=None):
        json_data = {
            'operation': 'declare_relationships',
            'scope': scope,
            'type': type,
            'key': key,
            'relationships': relationships
        }
        return self._put(account_id, deployment_id, json_data)
        
    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-RemoveAsset
        :type type: string
        :param type: The type of the asset being created.
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type: key: string
        :param key: The opaque, unique key for this asset, such as "/aws/us-east-1/host/i-1234567". The key and type parameters form a unique identifier for any asset.
    '''
    def remove_asset(self, deployment_id, scope, type, key, account_id=None):
        json_data = {
            'operation': 'remove_asset',
            'scope': scope,
            'type': type,
            'key': key
        }
        return self._put(account_id, deployment_id, json_data)

    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-RemoveAssets
        :type deployment_id: string
        :param deployment_id: The ID of the deployment source as represented in the deployments service
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type assets: list
        :param assets: An array of dictionaries with the keys type and key set for each asset to delete.

    '''
    def remove_assets(self, deployment_id, scope, assets, account_id=None):
        json_data = {
            'operation': 'remove_assets',
            'scope': scope,
            'assets': assets
        }
        return self._put(account_id, deployment_id, json_data)

    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-RemoveProperties
        :type type: string
        :param type: The type of the asset being updated.
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type: key: string
        :param key: The opaque, unique key for this asset, such as "/aws/us-east-1/host/i-1234567". The key and type parameters form a unique identifier for any asset.
        :type property_names: list
        :param property_names: A list of property names to remove; these can either be strings or lists of strings for nested property paths. Property names may only be composed of characters [a-zA-Z0-9_].
    '''
    def remove_properties(self, deployment_id, scope, type, key, account_id=None):
        json_data = {
            'operation': 'remove_properties',
            'scope': scope,
            'type': type,
            'key': key,
            'property_names': property_names
        }
        return self._put(account_id, deployment_id, json_data)

    '''
        https://console.account.alertlogic.com/users/api/assets_write/#api-DeclareModify-RemoveRelationships
        :type type: string
        :param type: The type of the asset being updated.
        :type scope: string
        :param scope: The declaring software's authority or area of function. The scope must match the regex pattern [0-9A-Za-z-].
        :type: key: string
        :param key: The opaque, unique key for this asset, such as "/aws/us-east-1/host/i-1234567". The key and type parameters form a unique identifier for any asset.
        :type relationships: list
        :param relationships: A list of Objects describing relationships to other assets. Each object in the list must have a "type" field and a "key" describing the type and key of asset the new or updated asset will have a relationship to.
    '''
    def remove_relationships(self, deployment_id, scope, type, key, account_id=None):
        json_data = {
            'operation': 'remove_relationships',
            'scope': scope,
            'type': type,
            'key': key,
            'relationship': relationship 
        }
        return self._put(account_id, deployment_id, json_data)


    def _put(self, account_id, deployment_id, json_data):
        return self.put(account_id=account_id,
                        path_parts=['deployments', deployment_id.upper(), 'assets'],
                        json_data=json_data)

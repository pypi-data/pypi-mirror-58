import os
import sys
import typing
import inspect
import logging
import pprint
import yaml
import json
import requests

class OpenAPIKeyWord:
    OPENAPI = "openapi"
    INFO = "info"

    SERVERS = "servers"
    URL = "url"
    SUMMARY = "summary"
    DESCRIPTION = "description"
    VARIABLES = "variables"
    REF = "$ref"
    REQUEST_BODY_NAME = "x-request-body-name"

    PATHS = "paths"
    OPERATION_ID = "operationId"
    PARAMETERS = "parameters"
    REQUEST_BODY = "requestBody"
    IN = "in"
    PATH = "path"
    QUERY = "query"
    HEADER = "header"
    COOKIE = "cookie"
    NAME = "name"
    REQUIRED = "required"
    SCHEMA = "schema"
    TYPE = "type"
    STRING = "string"
    OBJECT = "object"
    SECURITY = "security"
    COMPONENTS = "components"
    SCHEMAS = "schemas"
    PROPERTIES = "properties"
    REQUIRED = "required"
    CONTENT = "content"
    DEFAULT = "default"

    # ActiveWatch specific extensionso
    X_REQUEST_BODY = "x-activewatch-request-body"
    X_ACTIVEWATCH_SESSION_ENDPOINT = "x-activewatch-session-endpoint"

class Server(object):
    _url: str
    description: str
    variables: typing.Dict[str, typing.Any]

    def __init__(self, service_name,
            url=None, description=None,
            variables=None,
            variables_spec=None,
            aw_session_endpoint=False,
            session = None):
        self._service_name = service_name
        self.description = description
        self.variables = variables or variables_spec and dict((k, v.get(OpenAPIKeyWord.DEFAULT)) for (k, v) in variables_spec.items()) or None

        # ActiveWatch extention to use Global Endpoint
        self._url = aw_session_endpoint and session and session.get_url(self._service_name) or url
        print(f"URL: {self._url}")
        print(f"Variables: {self.variables}")

    @property
    def url(self):
        if self.variables:
            return self._url.format(**self.variables)
        else:
            return self._url

    def set_url(self, url):
        self._url = url

class RequestBody(object):
    def __init__(self, content_type, model, x_request_body=None):
        # print("RequestBody:__init__(): {}, {}, {}".format(content_type, model, x_request_body))
        data_type = model.pop(OpenAPIKeyWord.TYPE)
        if not data_type:
            raise ValueError(f"'{OpenAPIKeyWord.TYPE}' is not a missing")

        self._x_request_body = x_request_body
        if data_type == OpenAPIKeyWord.OBJECT:
            self._required = model.pop(OpenAPIKeyWord.REQUIRED, [])
            self._properties = model.pop(OpenAPIKeyWord.PROPERTIES)
            self._type = OpenAPIKeyWord.OBJECT
        else:
            raise ValueError(f"'{data_type}' is not a supported model type")
        
        self._content_type = content_type
    
    def serialize(self, headers, kwargs):
        body = {}
        if self._type == OpenAPIKeyWord.OBJECT:
            if self._x_request_body:
                param_name = self._x_request_body.pop(OpenAPIKeyWord.NAME)
                if param_name not in kwargs and len(self._required):
                    raise ValueError(f"'{name}' is required")
                body = kwargs.pop(param_name)
                if not all(name in body for name in self._required):
                    raise ValueError(f"'{self._required}' are required in '{param_name}'")
            else:
                if not all(name in kwargs for name in self._required):
                    raise ValueError(f"'{self._required}' are required'")
                for property_name, property_type in self._properties.items():
                    if property_name not in kwargs: continue
                    body[property_name] = kwargs.pop(property_name)

        headers['Content-Type'] = self._content_type 
        kwargs['data'] = json.dumps(body) 

class PathParameter(object):
    def __init__(self, spec = {}, defaults=None):
        self._in = spec[OpenAPIKeyWord.IN]
        self._name = spec[OpenAPIKeyWord.NAME]
        self._required = spec.get(OpenAPIKeyWord.REQUIRED, False)
        self._default = defaults and defaults.get(self._name)

    def serialize(self, path_params, query_params, headers, cookies, kwargs):
        if self._default: value = self._default
        if self._name not in kwargs and not self._default:
            if self._required:
                raise ValueError(f"'{self._name}' is required")
            return
        value = kwargs.pop(self._name, self._default)
        if self._in == OpenAPIKeyWord.PATH:
            path_params[self._name] = value
        elif self._in == OpenAPIKeyWord.QUERY:
            query_params[self._name] = value
        elif _in == OpenAPIKeyWord.HEADER:
            headers[self._name] = value
        elif _in == OpenAPIKeyWord.COOKIE:
            cookies[self._name] = value
       
        return True

class Operation(object):
    _internal_param_prefix = "_"
    _call: typing.Optional[typing.Callable] = None

    def __init__(self, path, ref, params, summary, description, method, spec, body, session=None, server=None):
        self._path = path
        self._ref = ref
        self._params = params
        self._summary = summary
        self._description = description
        self._method = method
        self._spec = spec
        self._body = body
        self._session = session
        self._server = server
        #self._defaults = session and session.get_defaults() or {}

    @property
    def spec(self):
        return self._spec

    @property
    def operation_id(self):
        return self._spec[OpenAPIKeyWord.OPERATION_ID]

    @property
    def method(self):
        return self._method

    @property
    def path(self):
        return self._path

    def url(self, **kwargs):
        return self._server.url + self._path.format(**kwargs)

    def _get_body(self, headers, body, kwargs):
        body_spec = self._spec.get(OpenAPIKeyWord.REQUEST_BODY)
        if not body_spec:
            return

        # TODO: If requestBody has a non-refed object, use it's properties and ignore OpenAPIKeyWord.REQUEST_BODY_NAME
        name = body_spec.get(OpenAPIKeyWord.REQUEST_BODY_NAME, OpenAPIKeyWord.REQUEST_BODY)

        content = body_spec.get(OpenAPIKeyWord.CONTENT)
        if not content:
            raise ValueError(f"'{OpenAPIKeyWord.CONTENT}' is required for '{OpenAPIKeyWord.REQUEST_BODY}'")
        
        # for now get the first content type
        content_type, schema_spec = content.popitem()
        headers.update({"Content-Type": content_type})
        ref = schema_spec[OpenAPIKeyWord.SCHEMA].get(OpenAPIKeyWord.REF)
        if ref:
            parts = ref.split('/')
            t = getattr(sys.modules[__name__], parts[3])

    def _gen_call(self):
        def f(**kwargs):
            path_params = {}
            params = {}
            headers = {}
            cookies = {}
            body = {}
            
            # Set operation specific parameters
            for param in self._params:
                param.serialize(path_params, params, headers, cookies, kwargs)

            if self._body:
                self._body.serialize(headers, kwargs)

            # collect internal params
            for k in kwargs:
                if not k.startswith(self._internal_param_prefix):
                    continue
                kwargs[
                    k[len(self._internal_param_prefix) :]  # noqa: E203
                ] = kwargs.pop(k)
            
            kwargs.setdefault("params", {}).update(params)
            kwargs.setdefault("headers", {}).update(headers)
            kwargs.setdefault("cookies", {}).update(cookies)

            print("Calling [{}: {}]: {}".format(self.url(**path_params), self._method, kwargs))
            return self._session.request(
                self._method, self.url(**path_params), **kwargs
            )
            
        return f
            

    def __call__(self, *args, **kwargs):
        if not self._call:
            self._call = self._gen_call()
        return self._call(*args, **kwargs)

    def help(self):
        return pprint.pprint(self.spec, indent=2)

    def __repr__(self):
        return f"<{type(self).__name__}: [{self._method}] {self._path}>"

class Client(object):
    _operations: typing.Dict[str, typing.Any]
    _spec: typing.Dict[str, typing.Any]
    _models: typing.Dict[str, typing.Any]

    def __init__(self, name, version='v1', session=None, residency=None, variables=None):
        api_dir = f"{os.path.dirname(__file__)}/apis"
        self._name = name
        self._server = None
        self._session = session
        self._residency = residency
        self._operations = {}
        self._spec = {}
        self._models = {}
        self._defaults = session and session.get_defaults() or {}
        spec = self.load_spec_from_file(f"{api_dir}/{name}.{version}.yaml")
        self.load_spec(spec, variables)

    @property
    def server(self):
        return self._server

    def set_server(self, s):
        self._server = s
        self._initialize_operations()

    @property
    def operations(self):
        return self._operations

    @property
    def spec(self):
        return self._spec

    def load_spec(self, spec: typing.Dict, variables: typing.Dict):
        if not all(
            [
                i in spec
                for i in [
                    OpenAPIKeyWord.OPENAPI,
                    OpenAPIKeyWord.INFO,
                    OpenAPIKeyWord.PATHS,
                ]
            ]
        ):
            raise ValueError("Invaliad openapi document")

        self._spec = spec.copy()
        _spec = spec.copy()

        servers = _spec.pop(OpenAPIKeyWord.SERVERS, [])
        for key in _spec:
            rkey = key.replace("-", "_")
            self.__setattr__(rkey, _spec[key])

        self.servers = [
            Server(
                service_name=self._name,
                url=s.get(OpenAPIKeyWord.URL),
                description=s.get(OpenAPIKeyWord.DESCRIPTION),
                variables=variables,
                variables_spec=s.get(OpenAPIKeyWord.VARIABLES),
                aw_session_endpoint=s.get(OpenAPIKeyWord.X_ACTIVEWATCH_SESSION_ENDPOINT, False),
                session=self._session
            )
            for s in servers
        ]

        if not self._server and self.servers:
            self._server = self.servers[0]

        self._initialize_operations()
    
    def _initialize_operations(self):
        self._operations = {}
        for path, path_spec in self.paths.items():
            ref = path_spec.pop(OpenAPIKeyWord.REF, "") #TODO: Add ref handler

            params = [
                PathParameter(
                    spec = param_spec,
                    defaults = self._defaults
                )
                for param_spec in path_spec.pop(OpenAPIKeyWord.PARAMETERS, [])
            ]

            summary = path_spec.pop(OpenAPIKeyWord.SUMMARY, "")
            description = path_spec.pop(OpenAPIKeyWord.DESCRIPTION, "")

            for method, op_spec in path_spec.items():
                operation_id = op_spec.get(OpenAPIKeyWord.OPERATION_ID)
                if not operation_id:
                    logging.warn(
                        f"'{OpenAPIKeyWord.OPERATION_ID}' not found in: '[{method}] {path}'"
                    )
                    continue

                params.extend([
                    PathParameter(
                        spec = param_spec,
                        defaults = self._defaults
                    )
                    for param_spec in op_spec.get(OpenAPIKeyWord.PARAMETERS, [])
                ])

                body = self._initalize_request_body(op_spec.get(OpenAPIKeyWord.REQUEST_BODY, None))

                op_body = op_spec.pop(OpenAPIKeyWord.REQUEST_BODY, None)
                if operation_id not in self._operations:
                    self._operations[operation_id] = Operation(
                        path,
                        ref,
                        params,
                        summary,
                        description,
                        method,
                        op_spec,
                        body,
                        session = self._session,
                        server = self._server
                    )
                else:
                    v = self._operations[operation_id]
                    if type(v) is not list:
                        self._operations[operation_id] = [v]
                    self._operations[operation_id].append(
                        Operation(
                            path,
                            ref,
                            params,
                            summary,
                            description,
                            method,
                            op_spec,
                            body,
                            session = self._session,
                            server = self._server
                        )
                    )

    def _initalize_request_body(self, body_spec = None):
        if not body_spec: return None 
        
        content = body_spec.pop(OpenAPIKeyWord.CONTENT, {})
        content_type, schema_spec = content.popitem()
        schema = schema_spec.pop(OpenAPIKeyWord.SCHEMA)
        ref = schema.pop(OpenAPIKeyWord.REF, None)

        if ref:
            # Get model object definitions
            if ref[:2] == '#/' and ref:
                parts = ref[2:].split('/')
                model = get_dict_value(self._spec, parts)
                return RequestBody(
                        content_type,
                        model,
                        x_request_body=body_spec.pop(OpenAPIKeyWord.X_REQUEST_BODY, None)
                    )
        else:
            return RequestBody(
                content_type = content_type,
                model = schema)

        return None

    def _initialize_type(self, type_name, type_spec):
        attributes = {
                "__init__": type_init_fun,
                "_required": type_spec.pop(OpenAPIKeyWord.REQUIRED, [])
            }
        properties = type_spec.pop(OpenAPIKeyWord.PROPERTIES, [])
        for property in properties:
            attributes.update({property.replace("-", "_"): None})

        Type = type(type_name, (OpenApiModelClass,), attributes)
        self._models.update({"#/components/schemas/{}".format(type_name): Type})

        # Make this class visible
        setattr(sys.modules[Type.__module__], Type.__name__, Type)

    def load_spec_from_file(self, file_path):
        print("Loading '{}' API spec file".format(file_path))
        with open(file_path) as f:
            spec = f.read()

        return yaml.load(spec, Loader=yaml.Loader)

    def __getattr__(self, op_name):
        if op_name in self._operations:
            return self._operations[op_name]
        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{op_name}'"
        )

'''
'''
class OpenApiModelClass(object):
    def _get_properties(self):
        pr = {}
        for name in dir(self):
            value = getattr(self, name)
            # ignore our internal and system generated properties
            if not name.startswith('_') and not inspect.ismethod(value):
                pr[name] = value
        return pr

    def to_json(self):
        return json.dumps(self._get_properties())

def type_init_fun(self, *argc, **kwargs):
    for param_name in self._required:
        if param_name not in kwargs:
            raise ValueError(f"'{param_name}' is required")
        setattr(self, param_name, kwargs.pop(param_name))

    for param_name, value in kwargs.items():
        if not hasattr(self, param_name):
            raise ValueError(f"'{param_name}' is not a valid paramter")
        setattr(self, param_name, value)

def get_dict_value(dict, list, default=None):
    length = len(list)
    try:
        for depth, key in enumerate(list):
            if depth == length - 1:
                output = dict[key]
                return output
            dict = dict[key]
    except (KeyError, TypeError):
        return default
    return default


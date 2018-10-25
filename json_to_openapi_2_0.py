"""Convert an Onshape endpoints definition JSON to a Swagger 2.0 API specification file."""

from ruamel.yaml import YAML
import pathlib
import json
import re

yaml = YAML()


class Converter:
    """This class is broken into two types of functions, those with the @property decorator and those with the
    @staticmethod decorator. The @property classes depend fully on the state of the converter instance, and
    represent intermediate states of process between the initial and converted state. These intermediate states
    can be useful for debugging, logical encapsulation, etc... By making them properties, we ensure that no
    one will senselessly duplicate state. On the other hand, @staticmethod classes can be thought of as
    utility classes that can convert one small piece of json to swagger very well. As such, they have no
    dependence on the converter's instance state."""

    default_config = {'visible_permissions': ['public'], 'show_deprecated': False, 'method_fixer_path': None,
                      'include_required': False, 'include_tags': False}
    """A configuration dictionary that can get altered as needed and passed into the constructor with the 'config' 
    keyword. These are the following keys:
    
    'visible_permissions': a list of permission scopes that the methods need to have in order to be parsed into the 
        swagger spec.
    'show_deprecated': a bool that if false, prevents the parsing of deprecated methods. Otherwise parse deprecated.
    'method_fixer_path': a file path that points to a YAML of a list of paths that should overwrite the parsed 
        methods/paths.
    'include_required': Whether or not to include the 'required' key in the response and parameter model description.
        We have not consistently applied the required key in our source documentation, so we can't depend on our own
        required flag."""

    def __init__(self, path="./apiData.json", template_path="onshapeOpenApiSpecTemplate.yaml", config=default_config):
        self.template_path = template_path
        self.path = path
        self.config = Converter.default_config
        self.config.update(config)


    @property
    def json_dict(self):
        """Return the dict read from self.path"""
        return json.load(open(self.path))

    @property
    def filtered_endpoints(self):
        """Return the list of filtered endpoints as filtered according to the values set in the configuration"""
        l = []
        for group in self.json_dict:
            for endpoint in group['endpoints']:
                # collect statuses of current endpoint
                deprecated = any(['deprecated' in p['name'] for p in endpoint['permission']])
                # Filter out any endpoints that should be skipped based on config settings
                has_visible_permission_scope = [p in endpoint['permission'][0]['name'] for p in
                                                self.config['visible_permissions']]
                # Filter through the various criteria and set the allowed flag if any configuration criteria is not met:
                allowed = True
                if not any(has_visible_permission_scope):
                    allowed = False
                if not self.config['show_deprecated'] and deprecated:
                    allowed = False

                if allowed:
                    l.append(endpoint)
        return l

    @property
    def template_dict(self):
        """Return the dict read from self.template_path"""
        return yaml.load(open(self.template_path))

    @property
    def models_dict(self):
        """Return a dict that makes a best guess at constructing all the potential data models from the success and
        descriptions present in the body and the response"""
        d = {}
        for endpoint in self.filtered_endpoints:
            if "success" in endpoint and "fields" in endpoint["success"] and "Response" in endpoint["success"][
                "fields"]:
                model, required = Converter.convert_response_list_to_definition(
                    endpoint["success"]["fields"]["Response"])
                if model['type'] == 'object':
                    d[Converter.name_model(endpoint, self.ModelLocations.RESPONSE_200)] = model
            if "parameter" in endpoint and "fields" in endpoint["parameter"] and "Body" in endpoint["parameter"][
                "fields"]:
                model, required = Converter.convert_response_list_to_definition(
                    [b for b in endpoint["parameter"]["fields"]["Body"] if b['type'] != 'File'])
                if model['type'] == 'object':
                    d[Converter.name_model(endpoint, self.ModelLocations.BODY)] = model
                    if len(required) < 0:
                        d[Converter.name_model(endpoint, self.ModelLocations.BODY)]['required'] = required
        return d

    @property
    def method_dict(self):
        """Parse a json file made with the onshape JSON 'spec' into a valid set of swagger operation items, such that
        d = {(path, method): operation_definition}"""
        d = {}

        for endpoint in self.filtered_endpoints:


            # Assemble the openApi (path,method) dict.
            method = endpoint['type']
            path = Converter.convert_path(endpoint['url'])

            # Get the implicit path parameters like [wvm] into the parameter list.
            path, param_list = Converter.convert_bracketed_path_components_to_parameter_list(path)

            v = {}
            # The parameters that relate to a single endpoint (path, method pair)
            v["summary"] = endpoint['title']
            v['operationId'] = endpoint['name'] + endpoint['group']
            v['description'] = endpoint['description']
            v["parameters"] = param_list
            if self.config['include_tags']:
                v["tags"] = [endpoint['group']]
            oauth = []
            for permission_dict in endpoint['permission']:
                oauth = []
                permission = permission_dict['name']
                if "OAuth" in permission:
                    oauth.append(permission)
                # Apply the deprecated tag
                elif "deprecated" in permission:
                    v["deprecated"] = True
                    try:
                        # Add the replaced with line to the description
                        v['description'] += "This endpoint has been replaced! Please use:" + \
                                            endpoint['error']['fields']['ReplacedBy'][0]['description']
                    except KeyError as e:
                        raise KeyError("The replacement URL should be added under {}.")
                # Apply an x-public tag that is responsible for hiding the endpoints not marked with 'x-public'
                # with a Swagger extension.
                # elif 'public' in permission and self.config['include_tags']:
                #     v['tags'].append('x-public')
            v['security'] = [{"OAuth2": oauth}, {"apiSecretKey": []}, {"apiAccessKey": []}]

            # Parse the fields in the field list into the parameter list
            if 'parameter' in endpoint and 'fields' in endpoint['parameter']:
                for type, field_list in endpoint['parameter']['fields'].items():
                    # Do some munging to get the body params into the correct arrangement.
                    if type == "Body":
                        # Awkwardly detect if this is indeed a file (and thus should have the multipart form data)
                        if any([(f['type'] == "File") for f in field_list]):
                            v["parameters"] += (Converter.convert_form_list_to_form_data_list(field_list))
                            v["consumes"] = ["multipart/form-data"]
                        else:
                            body_param = {"in": "body", "name": "Body", "description": "The JSON request body."}
                            body_param['schema'] = {'$ref': Converter.ref_model(endpoint)}
                            v["parameters"].append(body_param)
                    else:
                        v["parameters"] += (Converter.convert_field_list_to_parameter_list(field_list))
            # For annotated successful responses.
            if "success" in endpoint and "fields" in endpoint["success"] and "Response" in endpoint["success"][
                "fields"]:
                response_list = endpoint["success"]["fields"]["Response"]
                # This is a special endpoint that returns an array instead of an object
                if endpoint['name'] == "getEndpoints":
                    v["responses"] = {"200":
                                          {"description": 'OK',
                                           "schema":
                                               {'type': 'array',
                                                'description': 'Array containing response data.',
                                                'items': {'type': 'object', 'description': 'Endpoint object.'}}}}
                elif len(response_list) == 1 and response_list[0]["type"] == 'Data':
                    v["responses"] = {"200":
                                          {"description": response_list[0]['description'],
                                           'schema': {"type": "file"}}}
                elif len(response_list) == 1 and response_list[0]["type"] == 'File':
                    v["responses"] = {"200":
                                          {"description": response_list[0]['description'],
                                           'schema': {"type": "file"}}}
                else:
                    model_name = Converter.name_model(endpoint, self.ModelLocations.RESPONSE_200)
                    v["responses"] = {"200":
                                          {"description": 'OK',
                                           "schema":
                                               {'$ref': '#/definitions/{}'.format(model_name)}}}


            # If the response is not annotated, we need to generate one based on the method type
            else:
                if endpoint['type'] == 'delete':
                    v["responses"] = {"200": {'description': 'The resource was successfully deleted'}}
                else:
                    v["responses"] = {"200": {'description': "This endpoint's response is not documented."}}
            d[(path, method)] = v
        # Add the methods specified in the yaml at method_fixer_path to the method dict.
        if 'method_fixer_path' in self.config and self.config['method_fixer_path']:
            for path in yaml.load(open(self.config['method_fixer_path'])):
                for method in path:
                    d[(path, method)] = v
        return d

    @property
    def filtered_method_dict(self):
        """Filter the method dict based on the configuration. TODO: pull out the filtering logic into this method."""
        config = self.config
        d = self.method_dict
        pass

    @property
    def paths_dict(self):
        """A dictionary where each key is a path. This dictionary should be what Swagger is expecting under the path
        key."""
        paths = {}
        for (path, method), v in self.method_dict.items():
            if path not in paths:
                paths[path] = {method: v}
            else:
                paths[path].update({method: v})
        return paths

    @property
    def converted_dict(self):
        """The dictionary in the form that Swagger expects."""
        d = self.template_dict
        paths = self.paths_dict
        d['paths'] = paths
        d['definitions'] = self.models_dict
        return d

    @staticmethod
    def convert_response_list_to_definition(response_list, include_required=True, include_required_recursive=False):
        """Convert a response list, such as:
            [
                      {
                        "group": "Response",
                        "type": "Object[]",
                        "optional": false,
                        "field": "configurationParameters"
                      },
                      {
                        "group": "Response",
                        "type": "Object",
                        "optional": false,
                        "field": "configurationParameters.0"
                      },
                      {
                        "group": "Response",
                        "type": "Object[]",
                        "optional": false,
                        "field": "currentConfiguration"
                      },
                      {
                        "group": "Response",
                        "type": "Object",
                        "optional": false,
                        "field": "currentConfiguration.0"
                      },
                      {
                        "group": "Response",
                        "type": "String",
                        "optional": false,
                        "field": "serializationVersion"
                      },
                      {
                        "group": "Response",
                        "type": "String",
                        "optional": false,
                        "field": "sourceMicroversion",
                      }
            ]
            into a dict of Schemas, like:
            ---
            confiigurationParameters:
                required: true
                type: array
                items:
                    $ref: '#/definitions/configurationParameter'
            configurationParameter:
                type: object
            currentConfiguration:
                type: array
                required: true
                items:
                    $ref: '#/definitions/configurationParameter'
            currentConfigurationElement:
                type: object
                required: true
            serializationVersion:
                required: True
                type: string
            sourceMicroversion:
                required: True
                type: string
            ---

            This guarantees that if another element is used as a reference, it has the specifications dictated
            correctly. That way, one definition cannot depend on another that is actually different. We use the
            definition passed in thus far. We also pass the list of required fields.
            """
        d = {}
        required = []
        for response in response_list:
            # find where to insert the value
            path_list = Converter.response_name_to_path_list(response['field'])
            # find the type of the value to insert
            t = Converter.convert_type(response["type"])
            # If the type is returned as nothing, skip this response
            if not t:
                continue
            else:
                v = {}
                # Update the type
                v.update(t)

                if "description" in response:
                    v["description"] = response["description"]

            Converter.nested_set_update(d, path_list, v)

            # add to the required list or one level up from the path list.
            if not response["optional"]:
                if include_required_recursive:
                    if len(path_list) > 2:
                        two_levels_up = Converter.nested_get(d, path_list[:-2])
                        if 'type' in two_levels_up and two_levels_up['type'] == "object":
                            Converter.add_required(d, path_list[:-2], path_list[-1])
                # If there is only one item in the path_list, this must be a top level key, and we should insert it into
                # a list of top level required keys
                elif len(path_list) == 1 and include_required:
                    required.append(path_list[-1])

        # This is to deal with when the type is communicated within the key. Defaults to object.
        if len(d) == 1 and next(iter(d.values()))["type"] == 'file':
            d_final = d['file']
        elif len(d) == 1 and next(iter(d.values()))["type"] == 'data':
            d_final = d['data']
        else:
            d_final = {'type': 'object', 'properties': d}

        return d_final, required

    @staticmethod
    def parse_response_headers(header_list):
        """Translate a header list into a list of swagger header objects. Example:

        [
              {
                "group": "Header",
                "type": "String",
                "optional": false,
                "field": "Content-Type",
                "defaultValue": "application/json",
                "description": "Content type"
              },
              {
                "group": "Header",
                "type": "String",
                "optional": false,
                "field": "Accept",
                "defaultValue": "application/vnd.onshape.v1+json",
                "description": "Request JSON data response using version 1\n  request/response behavior"
              }
        ]

        ==>
        [
            {
                "Content-Type": {
                    "description": "Content type",
                    "type": "string",
                    "default": "application/json"
                },
                "Accept": {
                    "description": "Request JSON data response using version 1\n  request/response behavior",
                    "type": "string",
                    "default": "application/vnd.onshape.v1+json"
                }
            }
        ]
        """
        outer_d = {}
        for header in header_list:
            d = {}
            if 'description' in header:
                d['description'] = header['description']
            if 'defaultValue' in header:
                d['default'] = header['defaultValue']
            if 'type' in header:
                d['type'] = Converter.convert_type(header['type'])['type']
            outer_d[header['field']] = d
        return outer_d



    @staticmethod
    def add_required(dic, keys, value):
        """append a 'required' value onto a list accessed by a list of keys within a dic."""
        # Ensure all keys in keys list are present
        for key in keys:
            dic = dic.setdefault(key, {})
        if 'required' in dic:
            dic['required'].append(value)
        else:
            dic['required'] = [value]

    @staticmethod
    def nested_set_update(dic, keys, value):
        """Set a value in a dictionary based on the list of keys pointing to that value, or update the value if it
        points to a dictionary."""
        # Ensure all keys in keys list are present
        for key in keys[:-1]:
            dic = dic.setdefault(key, {})
        if keys[-1] not in dic:
            dic[keys[-1]] = value
        elif isinstance(value, dict) and isinstance(dic[keys[-1]], dict):
            dic[keys[-1]].update(value)

    @staticmethod
    def nested_get(input_dict, nested_key):
        """Get a key based on the list of keys."""
        internal_dict_value = input_dict
        for k in nested_key:
            internal_dict_value = internal_dict_value.get(k, None)
            if internal_dict_value is None:
                return None
        return internal_dict_value

    @staticmethod
    def response_name_to_path_list(name):
        """Change a response name to a list of keys (the 'path') to the item in the models dict,
        example:
        features.0.message --> ['features', 'items', 'properties', 'message']"""
        name_list = name.split(".")
        l = [name_list[0]]
        for i, name in enumerate(name_list[1:]):
            # If the name is a number, it represents an item in the list and we should replace it with an "items" key.
            if name.isdigit():
                l.append('items')
            # Else if it is a name, this must be an object, and so we need to add a "properties" key before it.
            else:
                l.append("properties")
                l.append(name)
        return l

    @staticmethod
    def convert_form_list_to_form_data_list(form_list):
        """Used to turn the form_list into a swagger list of parameters"""
        fl = []
        for field in form_list:
            f = {}
            f['in'] = 'formData'
            f['name'] = field['field']
            f.update(Converter.convert_type(field['type']))
            f['required'] = not field['optional']
            f['description'] = field['description']
            fl.append(f)
        return fl

    @staticmethod
    def convert_field_list_to_parameter_list(field_list):
        fl = []
        for field in field_list:
            f = {}
            f['name'] = field['field']
            if Converter.convert_type(field['group']):
                f['in'] = Converter.convert_type(field['group'])["type"]
            f['type'] = Converter.convert_type(field['type'])["type"]
            f['required'] = not field['optional']
            f['description'] = field['description']
            fl.append(f)
        return fl

    @staticmethod
    def convert_path(path):
        """
        "/accounts/:aid/purchases/:pid" -->  "/accounts/{aid}/purchases/{pid}"
        """
        return re.sub(r":(\w*)", r"{\1}", path)

    @staticmethod
    def convert_type(field_type):
        """ Match Onshape format endpoint strings to standard swagger types. Note that this returns a dictionary
        of swagger definition that can describe the type, examples are:
        "QueryParam" --> {'type': 'query'}
        "Date" --> {'type': 'string', 'format': "date-time"}
        The metatype parameter refers to which type matcher to use - primitive, or parameter
        """
        match = {"QueryParam": {'type': "query"}, "Body": {'type': "body"}, "PathParam": {'type': "path"},
                 "String": {'type': "string"}, "Boolean": {'type': "boolean"},
                 "Number[]": {'type': "array", 'items': {'type': "number"}}, "Number": {'type': "number"},
                 "Object[]": {'type': "array", 'items': {'type': "object"}},
                 "Object": {'type': "object"}, "String[]": {'type': "array", 'items': {'type': "string"}},
                 "File": {'type': "file"}, "Date": {'type': 'string', 'format': "date-time"},
                 "Data": {'type': "null"}, "Number[][]": {'type': "array", 'items': {'type': "number"}}}
        # Throw out null types
        if field_type == "null":
            return None
        return match[field_type]

    @staticmethod
    def convert_bracketed_path_components_to_parameter_list(path):
        """Takes in an endpoint like "/assemblies/d/{did}/[wvm]/{wvm}/e/{eid}" and turns all the bracketed path
        components, like [wvm] into a parameter definition that looks like:
        -name: wvm
         in: path
         type: string
         required: true
         description: "One of "w" or "v" corresponding to whether a "workspace" or "version" was entered. """

        # Get all items that match a bracketed string within the path
        bracket_catcher = re.compile(r"\[(\w*)\]")
        match_list = re.findall(bracket_catcher, path)

        # Conversion dictionary from bracketed character to the whole word
        map = {"w": "workspace", "v": "version", "m": "microversion", "c": "company", "u": "user", "d": "document"}
        param_list = []
        # Used to confirm that these path params are differentiated from the other path params - no collisions between
        # {wvm} and the converted [wvm].
        char_identifier_suffix = "_char"
        if match_list:
            for match in match_list:
                p = {"name": match + char_identifier_suffix,
                     "in": "path",
                     "type": "string",
                     "required": True}
                # Build the description
                try:
                    p["description"] = "One of {} corresponding to whether a {} was entered." \
                        .format(" or ".join([c for c in match]), " or ".join([map[c] for c in match]))
                except KeyError as e:
                    raise KeyError("The character {} was not mapped for endpoint {}.".format(e.args, path))
                param_list.append(p)
            path = re.sub(bracket_catcher, r"{\1" + char_identifier_suffix + "}", path)
        return path, param_list

    from enum import Enum

    class ModelLocations(Enum):
        BODY = "Body"
        RESPONSE_200 = "Response200"

    @staticmethod
    def name_model(endpoint, location=ModelLocations.BODY):
        """Takes an Onshape endpoint and provides a string that can be used to uniquely identify the method. If two
        endpoints provide the same value under here, that is a problem."""
        return "{group}_{name}_{location}".format(group=endpoint['group'], name=endpoint['name'], location=location.value)

    @staticmethod
    def ref_model(endpoint, location=ModelLocations.BODY):
        """Make a ref, like '#/definitions/Documents_getDocuments_Body'"""
        return "#/definitions/{}".format(Converter.name_model(endpoint, location))



if __name__ == "__main__":
    converter = Converter(path='./api_data/apiDataAll.json', template_path='./api_data/onshapeOpenApiSpecTemplate.yaml', config={'include_required': True, 'include_tags': True})
    yaml.dump(converter.converted_dict, open(converter.path + "Auto.yaml", "w"))

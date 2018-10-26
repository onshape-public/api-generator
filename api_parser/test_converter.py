from api_parser.json_to_openapi_2_0 import Converter
from ruamel.yaml import YAML
import pytest

yaml = YAML()


@pytest.mark.parametrize("response_list, expected, required_expected, include_required", [
    # Config params test
    ([
         {
             "group": "Response",
             "type": "Object[]",
             "optional": False,
             "field": "configurationParameters"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": False,
             "field": "configurationParameters.0"
         },
         {
             "group": "Response",
             "type": "Object[]",
             "optional": False,
             "field": "currentConfiguration"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": False,
             "field": "currentConfiguration.0"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "serializationVersion"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "sourceMicroversion",
         }
     ],
     {'type': 'object', 'properties': {'configurationParameters': {'type': 'array', 'items': {'type': 'object'}},
                                       'currentConfiguration': {'type': 'array', 'items': {'type': 'object'}},
                                       'serializationVersion': {'type': 'string'},
                                       'sourceMicroversion': {'type': 'string'}}},
     ['configurationParameters', 'currentConfiguration', 'serializationVersion', 'sourceMicroversion'], True),
    # get purchases test
    ([
         {
             "group": "Response",
             "type": "Object[]",
             "optional": False,
             "field": "items",
             "description": "Information about purchases"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.id",
             "description": "Purchase Id"
         },
         {
             "group": "Response",
             "type": "String[]",
             "optional": False,
             "field": "items.0.userIds",
             "description": "User Ids"
         },
         {
             "group": "Response",
             "type": "String[]",
             "optional": False,
             "field": "items.0.consumedIds",
             "description": "Consumed Ids"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "items.0.seats",
             "description": "Number of seats"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.accountId",
             "description": "Account id"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.planId",
             "description": "Plan id"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "items.0.planType",
             "description": "Plan type (0-RECURRING, 1-CONSUMABLE, 2-ONE_TIME)"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.planName",
             "description": "Plan name"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.group",
             "description": "Group"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.applicationId",
             "description": "Application Id"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "items.0.state",
             "description": "Purchase state (1-DELETED, 2-CANCELED, 3-UNPAID, 4-PAST_DUE,\n            5-TRIALING, 6-ACTIVE, 7-CONSUMED)"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.canceledAt",
             "description": "Purchase canceled at"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.subscriptionEndAt",
             "description": "Subscription end at"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "items.0.amountCents",
             "description": "Amount cents"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": False,
             "field": "items.0.card",
             "description": "Card information"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.card.type",
             "description": "Card type"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "items.0.card.last4",
             "description": "Card last four digits"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "items.0.card.expYear",
             "description": "Card expiration year"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "items.0.card.expMonth",
             "description": "Card expiration month"
         }
     ], {'type': 'object', 'properties': {'items': {'type': 'array', 'items': {'type': 'object', 'properties': {
        'id': {'type': 'string', 'description': 'Purchase Id'},
        'userIds': {'type': 'array', 'items': {'type': 'string'}, 'description': 'User Ids'},
        'consumedIds': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Consumed Ids'},
        'seats': {'type': 'number', 'description': 'Number of seats'},
        'accountId': {'type': 'string', 'description': 'Account id'},
        'planId': {'type': 'string', 'description': 'Plan id'},
        'planType': {'type': 'number', 'description': 'Plan type (0-RECURRING, 1-CONSUMABLE, 2-ONE_TIME)'},
        'planName': {'type': 'string', 'description': 'Plan name'}, 'group': {'type': 'string', 'description': 'Group'},
        'applicationId': {'type': 'string', 'description': 'Application Id'}, 'state': {'type': 'number',
                                                                                        'description': 'Purchase state (1-DELETED, 2-CANCELED, 3-UNPAID, 4-PAST_DUE,\n            5-TRIALING, 6-ACTIVE, 7-CONSUMED)'},
        'canceledAt': {'type': 'string', 'description': 'Purchase canceled at'},
        'subscriptionEndAt': {'type': 'string', 'description': 'Subscription end at'},
        'amountCents': {'type': 'number', 'description': 'Amount cents'},
        'card': {'type': 'object', 'description': 'Card information',
                 'properties': {'type': {'type': 'string', 'description': 'Card type'},
                                'last4': {'type': 'string', 'description': 'Card last four digits'},
                                'expYear': {'type': 'number', 'description': 'Card expiration year'},
                                'expMonth': {'type': 'number', 'description': 'Card expiration month'}}}}},
                                                    'description': 'Information about purchases'}}}, ['items'], True),
    # get parts in partstudio
    ([
         {
             "group": "Response",
             "type": "Object[]",
             "optional": False,
             "field": "parts",
             "description": "Parts list"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": False,
             "field": "parts.0",
             "description": "Individual part"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.partId",
             "description": "Part ID"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.name",
             "description": "Part name"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.partQuery",
             "description": "Onshape internal use"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.elementId",
             "description": "Element ID"
         },
         {
             "group": "Response",
             "type": "Boolean",
             "optional": False,
             "field": "parts.0.isHidden",
             "description": "Part visibility"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": True,
             "field": "parts.0.appearance",
             "description": "Part appearance"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "parts.0.appearance.opacity",
             "description": "Part opacity"
         },
         {
             "group": "Response",
             "type": "Boolean",
             "optional": False,
             "field": "parts.0.appearance.isGenerated",
             "description": "Whether the appearance was set by the user or\n            generated by Onshape"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": False,
             "field": "parts.0.appearance.color",
             "description": "Part color"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "parts.0.appearance.color.red",
             "description": "Red RGB value"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "parts.0.appearance.color.blue",
             "description": "Blue RGB value"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "parts.0.appearance.color.green",
             "description": "Green RGB value"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": True,
             "field": "parts.0.material",
             "description": "Part material, if assigned"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": True,
             "field": "parts.0.material.libraryName",
             "description": "Name of the material library"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.material.id",
             "description": "Id of the material"
         },
         {
             "group": "Response",
             "type": "Object[]",
             "optional": False,
             "field": "parts.0.material.properties",
             "description": "Properties of the material"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.material.properties.0.name",
             "description": "Material property name"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.material.properties.0.units",
             "description": "Units of the material property value"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": True,
             "field": "parts.0.material.properties.0.description",
             "description": "Material property description"
         },
         {
             "group": "Response",
             "type": "Number",
             "optional": False,
             "field": "parts.0.material.properties.0.value",
             "description": "Material property value"
         },
         {
             "group": "Response",
             "type": "Object",
             "optional": True,
             "field": "parts.0.customProperties",
             "description": "Custom properties, if any"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.microversionId",
             "description": "Document microversion ID"
         },
         {
             "group": "Response",
             "type": "String",
             "optional": False,
             "field": "parts.0.bodyType",
             "description": "Part body type; can be 'solid', 'surface', or 'wire'"
         },
         {
             "group": "Response",
             "type": "Boolean",
             "optional": False,
             "field": "parts.0.isMesh",
             "description": "Whether the part is a mesh"
         }
     ], {'type': 'object', 'properties': {'parts': {'type': 'array',
                                                    'items': {'type': 'object', 'description': 'Individual part',
                                                              'properties': {'partId': {'type': 'string',
                                                                                        'description': 'Part ID'},
                                                                             'name': {'type': 'string',
                                                                                      'description': 'Part name'},
                                                                             'partQuery': {'type': 'string',
                                                                                           'description': 'Onshape internal use'},
                                                                             'elementId': {'type': 'string',
                                                                                           'description': 'Element ID'},
                                                                             'isHidden': {'type': 'boolean',
                                                                                          'description': 'Part visibility'},
                                                                             'appearance': {'type': 'object',
                                                                                            'description': 'Part appearance',
                                                                                            'properties': {'opacity': {
                                                                                                'type': 'number',
                                                                                                'description': 'Part opacity'},
                                                                                                           'isGenerated': {
                                                                                                               'type': 'boolean',
                                                                                                               'description': 'Whether the appearance was set by the user or\n            generated by Onshape'},
                                                                                                           'color': {
                                                                                                               'type': 'object',
                                                                                                               'description': 'Part color',
                                                                                                               'properties': {
                                                                                                                   'red': {
                                                                                                                       'type': 'number',
                                                                                                                       'description': 'Red RGB value'},
                                                                                                                   'blue': {
                                                                                                                       'type': 'number',
                                                                                                                       'description': 'Blue RGB value'},
                                                                                                                   'green': {
                                                                                                                       'type': 'number',
                                                                                                                       'description': 'Green RGB value'}}}}},
                                                                             'material': {'type': 'object',
                                                                                          'description': 'Part material, if assigned',
                                                                                          'properties': {
                                                                                              'libraryName': {
                                                                                                  'type': 'string',
                                                                                                  'description': 'Name of the material library'},
                                                                                              'id': {'type': 'string',
                                                                                                     'description': 'Id of the material'},
                                                                                              'properties': {
                                                                                                  'type': 'array',
                                                                                                  'items': {
                                                                                                      'type': 'object',
                                                                                                      'properties': {
                                                                                                          'name': {
                                                                                                              'type': 'string',
                                                                                                              'description': 'Material property name'},
                                                                                                          'units': {
                                                                                                              'type': 'string',
                                                                                                              'description': 'Units of the material property value'},
                                                                                                          'description': {
                                                                                                              'type': 'string',
                                                                                                              'description': 'Material property description'},
                                                                                                          'value': {
                                                                                                              'type': 'number',
                                                                                                              'description': 'Material property value'}}},
                                                                                                  'description': 'Properties of the material'}}},
                                                                             'customProperties': {'type': 'object',
                                                                                                  'description': 'Custom properties, if any'},
                                                                             'microversionId': {'type': 'string',
                                                                                                'description': 'Document microversion ID'},
                                                                             'bodyType': {'type': 'string',
                                                                                          'description': "Part body type; can be 'solid', 'surface', or 'wire'"},
                                                                             'isMesh': {'type': 'boolean',
                                                                                        'description': 'Whether the part is a mesh'}}},
                                                    'description': 'Parts list'}}},
     ['parts'], True),
    # Get external data
    ([
         {
             "group": "Response",
             "type": "Data",
             "optional": False,
             "field": "data",
             "description": "Requested data"
         }
     ], {'description': 'Requested data', 'type': 'data'}, None, True),
    # Export part to parasolid
    ([
              {
                "group": "Response",
                "type": "File",
                "optional": False,
                "field": "file",
                "description": "The exported document, as an attachment (could be text or binary depending on\n            parameters)"
              }
            ], {'type': 'file', 'description': 'The exported document, as an attachment (could be text or binary depending on\n            parameters)'}, None, True)
])
def test_convert_responses_to_models(response_list, expected, required_expected, include_required):
    scheme_dict, required = Converter.convert_response_list_to_definition(response_list,
                                                                          include_required=include_required)
    assert scheme_dict == expected
    assert required == required_expected


def test_nested_set_update():
    d = {}
    Converter.nested_set_update(d, ['person', 'address', 'city'], 'New York')
    assert d == {'person': {'address': {'city': 'New York'}}}


def test_response_name_to_path_list():
    assert Converter.response_name_to_path_list("features.0.message") == ['features', 'items', 'properties', 'message']


def test_parse_headers():
    header_list = [
        {
            "group": "Header",
            "type": "String",
            "optional": False,
            "field": "Content-Type",
            "defaultValue": "application/json",
            "description": "Content type"
        },
        {
            "group": "Header",
            "type": "String",
            "optional": False,
            "field": "Accept",
            "defaultValue": "application/vnd.onshape.v1+json",
            "description": "Request JSON data response using version 1\n  request/response behavior"
        }
    ]
    expected_result = {

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
    actual_result = Converter.parse_response_headers(header_list)
    assert actual_result == expected_result


def test_add_required():
    dic = {'a': {'b': {'c': 'c.a'}}}
    keys = ['a', 'b']
    value = "We need this!"
    Converter.add_required(dic, keys, value)
    assert dic == {'a': {'b': {'c': 'c.a', 'required': ['We need this!']}}}

def test_expand_dictionary():
    d= {'a': {'b': {'c': {'$ref': '#/a.2'}}}, 'a.2': 'answer'}
    d_actual = Converter.expand_yaml(d)
    d_expected = {'a': {'b': {'c': 'answer'}}, 'a.2': 'answer'}
    assert d_actual == d_expected
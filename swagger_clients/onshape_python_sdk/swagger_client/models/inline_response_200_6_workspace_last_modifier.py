# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse2006WorkspaceLastModifier(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, name=None, id=None):  # noqa: E501
        """InlineResponse2006WorkspaceLastModifier - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse2006WorkspaceLastModifier.  # noqa: E501

        Name of user who last modified workspace  # noqa: E501

        :return: The name of this InlineResponse2006WorkspaceLastModifier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2006WorkspaceLastModifier.

        Name of user who last modified workspace  # noqa: E501

        :param name: The name of this InlineResponse2006WorkspaceLastModifier.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse2006WorkspaceLastModifier.  # noqa: E501

        ID of user who last modified workspace  # noqa: E501

        :return: The id of this InlineResponse2006WorkspaceLastModifier.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2006WorkspaceLastModifier.

        ID of user who last modified workspace  # noqa: E501

        :param id: The id of this InlineResponse2006WorkspaceLastModifier.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2006WorkspaceLastModifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

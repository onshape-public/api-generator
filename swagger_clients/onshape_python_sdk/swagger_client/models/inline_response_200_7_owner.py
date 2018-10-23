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


class InlineResponse2007Owner(object):
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
        'type': 'float',
        'name': 'str',
        'id': 'str',
        'href': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'href': 'href'
    }

    def __init__(self, type=None, name=None, id=None, href=None):  # noqa: E501
        """InlineResponse2007Owner - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._name = None
        self._id = None
        self._href = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.id = id
        self.href = href

    @property
    def type(self):
        """Gets the type of this InlineResponse2007Owner.  # noqa: E501

        Owner's user type, which can be: 0: user 1: company 2: Onshape  # noqa: E501

        :return: The type of this InlineResponse2007Owner.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2007Owner.

        Owner's user type, which can be: 0: user 1: company 2: Onshape  # noqa: E501

        :param type: The type of this InlineResponse2007Owner.  # noqa: E501
        :type: float
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this InlineResponse2007Owner.  # noqa: E501

        Name of document owner  # noqa: E501

        :return: The name of this InlineResponse2007Owner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2007Owner.

        Name of document owner  # noqa: E501

        :param name: The name of this InlineResponse2007Owner.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse2007Owner.  # noqa: E501

        ID of document owner  # noqa: E501

        :return: The id of this InlineResponse2007Owner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2007Owner.

        ID of document owner  # noqa: E501

        :param id: The id of this InlineResponse2007Owner.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this InlineResponse2007Owner.  # noqa: E501

        URL of user page for document owner  # noqa: E501

        :return: The href of this InlineResponse2007Owner.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this InlineResponse2007Owner.

        URL of user page for document owner  # noqa: E501

        :param href: The href of this InlineResponse2007Owner.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

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
        if not isinstance(other, InlineResponse2007Owner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

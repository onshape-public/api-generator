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


class InlineResponse2009Elements(object):
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
        'id': 'str',
        'element_type': 'str',
        'type': 'str',
        'length_units': 'str',
        'angle_units': 'str',
        'mass_units': 'str',
        'thumbnail_info': 'object',
        'thumbnails': 'object'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'element_type': 'elementType',
        'type': 'type',
        'length_units': 'lengthUnits',
        'angle_units': 'angleUnits',
        'mass_units': 'massUnits',
        'thumbnail_info': 'thumbnailInfo',
        'thumbnails': 'thumbnails'
    }

    def __init__(self, name=None, id=None, element_type=None, type=None, length_units=None, angle_units=None, mass_units=None, thumbnail_info=None, thumbnails=None):  # noqa: E501
        """InlineResponse2009Elements - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._id = None
        self._element_type = None
        self._type = None
        self._length_units = None
        self._angle_units = None
        self._mass_units = None
        self._thumbnail_info = None
        self._thumbnails = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.element_type = element_type
        self.type = type
        self.length_units = length_units
        self.angle_units = angle_units
        self.mass_units = mass_units
        self.thumbnail_info = thumbnail_info
        self.thumbnails = thumbnails

    @property
    def name(self):
        """Gets the name of this InlineResponse2009Elements.  # noqa: E501

        Element name  # noqa: E501

        :return: The name of this InlineResponse2009Elements.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2009Elements.

        Element name  # noqa: E501

        :param name: The name of this InlineResponse2009Elements.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse2009Elements.  # noqa: E501

        Element ID  # noqa: E501

        :return: The id of this InlineResponse2009Elements.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2009Elements.

        Element ID  # noqa: E501

        :param id: The id of this InlineResponse2009Elements.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def element_type(self):
        """Gets the element_type of this InlineResponse2009Elements.  # noqa: E501

        Element type (for example, \"PARTSTUDIO\")  # noqa: E501

        :return: The element_type of this InlineResponse2009Elements.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this InlineResponse2009Elements.

        Element type (for example, \"PARTSTUDIO\")  # noqa: E501

        :param element_type: The element_type of this InlineResponse2009Elements.  # noqa: E501
        :type: str
        """
        if element_type is None:
            raise ValueError("Invalid value for `element_type`, must not be `None`")  # noqa: E501

        self._element_type = element_type

    @property
    def type(self):
        """Gets the type of this InlineResponse2009Elements.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The type of this InlineResponse2009Elements.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2009Elements.

        Onshape internal use  # noqa: E501

        :param type: The type of this InlineResponse2009Elements.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def length_units(self):
        """Gets the length_units of this InlineResponse2009Elements.  # noqa: E501

        Length units, for Part Studio and Assembly elements only  # noqa: E501

        :return: The length_units of this InlineResponse2009Elements.  # noqa: E501
        :rtype: str
        """
        return self._length_units

    @length_units.setter
    def length_units(self, length_units):
        """Sets the length_units of this InlineResponse2009Elements.

        Length units, for Part Studio and Assembly elements only  # noqa: E501

        :param length_units: The length_units of this InlineResponse2009Elements.  # noqa: E501
        :type: str
        """
        if length_units is None:
            raise ValueError("Invalid value for `length_units`, must not be `None`")  # noqa: E501

        self._length_units = length_units

    @property
    def angle_units(self):
        """Gets the angle_units of this InlineResponse2009Elements.  # noqa: E501

        Angle units, for Part Studio and Assembly elements only  # noqa: E501

        :return: The angle_units of this InlineResponse2009Elements.  # noqa: E501
        :rtype: str
        """
        return self._angle_units

    @angle_units.setter
    def angle_units(self, angle_units):
        """Sets the angle_units of this InlineResponse2009Elements.

        Angle units, for Part Studio and Assembly elements only  # noqa: E501

        :param angle_units: The angle_units of this InlineResponse2009Elements.  # noqa: E501
        :type: str
        """
        if angle_units is None:
            raise ValueError("Invalid value for `angle_units`, must not be `None`")  # noqa: E501

        self._angle_units = angle_units

    @property
    def mass_units(self):
        """Gets the mass_units of this InlineResponse2009Elements.  # noqa: E501

        Mass units, for Part Studio and Assembly elements only  # noqa: E501

        :return: The mass_units of this InlineResponse2009Elements.  # noqa: E501
        :rtype: str
        """
        return self._mass_units

    @mass_units.setter
    def mass_units(self, mass_units):
        """Sets the mass_units of this InlineResponse2009Elements.

        Mass units, for Part Studio and Assembly elements only  # noqa: E501

        :param mass_units: The mass_units of this InlineResponse2009Elements.  # noqa: E501
        :type: str
        """
        if mass_units is None:
            raise ValueError("Invalid value for `mass_units`, must not be `None`")  # noqa: E501

        self._mass_units = mass_units

    @property
    def thumbnail_info(self):
        """Gets the thumbnail_info of this InlineResponse2009Elements.  # noqa: E501

        Thumbnail information  # noqa: E501

        :return: The thumbnail_info of this InlineResponse2009Elements.  # noqa: E501
        :rtype: object
        """
        return self._thumbnail_info

    @thumbnail_info.setter
    def thumbnail_info(self, thumbnail_info):
        """Sets the thumbnail_info of this InlineResponse2009Elements.

        Thumbnail information  # noqa: E501

        :param thumbnail_info: The thumbnail_info of this InlineResponse2009Elements.  # noqa: E501
        :type: object
        """
        if thumbnail_info is None:
            raise ValueError("Invalid value for `thumbnail_info`, must not be `None`")  # noqa: E501

        self._thumbnail_info = thumbnail_info

    @property
    def thumbnails(self):
        """Gets the thumbnails of this InlineResponse2009Elements.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The thumbnails of this InlineResponse2009Elements.  # noqa: E501
        :rtype: object
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this InlineResponse2009Elements.

        Onshape internal use  # noqa: E501

        :param thumbnails: The thumbnails of this InlineResponse2009Elements.  # noqa: E501
        :type: object
        """
        if thumbnails is None:
            raise ValueError("Invalid value for `thumbnails`, must not be `None`")  # noqa: E501

        self._thumbnails = thumbnails

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
        if not isinstance(other, InlineResponse2009Elements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

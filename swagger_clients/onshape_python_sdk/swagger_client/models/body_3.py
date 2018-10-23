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


class Body3(object):
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
        'version_id': 'str',
        'microversion_id': 'str',
        'workspace_id': 'str',
        'name': 'str',
        'description': 'str',
        'read_only': 'bool',
        'client_interaction_mode': 'float'
    }

    attribute_map = {
        'version_id': 'versionId',
        'microversion_id': 'microversionId',
        'workspace_id': 'workspaceId',
        'name': 'name',
        'description': 'description',
        'read_only': 'readOnly',
        'client_interaction_mode': 'clientInteractionMode'
    }

    def __init__(self, version_id=None, microversion_id=None, workspace_id=None, name=None, description=None, read_only=None, client_interaction_mode=None):  # noqa: E501
        """Body3 - a model defined in Swagger"""  # noqa: E501

        self._version_id = None
        self._microversion_id = None
        self._workspace_id = None
        self._name = None
        self._description = None
        self._read_only = None
        self._client_interaction_mode = None
        self.discriminator = None

        if version_id is not None:
            self.version_id = version_id
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.name = name
        if description is not None:
            self.description = description
        if read_only is not None:
            self.read_only = read_only
        if client_interaction_mode is not None:
            self.client_interaction_mode = client_interaction_mode

    @property
    def version_id(self):
        """Gets the version_id of this Body3.  # noqa: E501

        Version ID of parent version  # noqa: E501

        :return: The version_id of this Body3.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this Body3.

        Version ID of parent version  # noqa: E501

        :param version_id: The version_id of this Body3.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def microversion_id(self):
        """Gets the microversion_id of this Body3.  # noqa: E501

        Microversion ID of parent document microversion  # noqa: E501

        :return: The microversion_id of this Body3.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this Body3.

        Microversion ID of parent document microversion  # noqa: E501

        :param microversion_id: The microversion_id of this Body3.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this Body3.  # noqa: E501

        Workspace ID of parent workspace  # noqa: E501

        :return: The workspace_id of this Body3.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this Body3.

        Workspace ID of parent workspace  # noqa: E501

        :param workspace_id: The workspace_id of this Body3.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def name(self):
        """Gets the name of this Body3.  # noqa: E501

        Workspace name (not required if readOnly=true)  # noqa: E501

        :return: The name of this Body3.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body3.

        Workspace name (not required if readOnly=true)  # noqa: E501

        :param name: The name of this Body3.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Body3.  # noqa: E501

        Workspace description  # noqa: E501

        :return: The description of this Body3.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body3.

        Workspace description  # noqa: E501

        :param description: The description of this Body3.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def read_only(self):
        """Gets the read_only of this Body3.  # noqa: E501

        Reserved for internal use  # noqa: E501

        :return: The read_only of this Body3.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Body3.

        Reserved for internal use  # noqa: E501

        :param read_only: The read_only of this Body3.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def client_interaction_mode(self):
        """Gets the client_interaction_mode of this Body3.  # noqa: E501

        Reserved for internal use  # noqa: E501

        :return: The client_interaction_mode of this Body3.  # noqa: E501
        :rtype: float
        """
        return self._client_interaction_mode

    @client_interaction_mode.setter
    def client_interaction_mode(self, client_interaction_mode):
        """Sets the client_interaction_mode of this Body3.

        Reserved for internal use  # noqa: E501

        :param client_interaction_mode: The client_interaction_mode of this Body3.  # noqa: E501
        :type: float
        """

        self._client_interaction_mode = client_interaction_mode

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
        if not isinstance(other, Body3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

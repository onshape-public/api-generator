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

from swagger_client.models.inline_response2001_created_by import InlineResponse2001CreatedBy  # noqa: F401,E501
from swagger_client.models.inline_response2001_modified_by import InlineResponse2001ModifiedBy  # noqa: F401,E501
from swagger_client.models.inline_response2001_thumbnail import InlineResponse2001Thumbnail  # noqa: F401,E501
from swagger_client.models.inline_response2002_default_workspace import InlineResponse2002DefaultWorkspace  # noqa: F401,E501
from swagger_client.models.inline_response2007_owner import InlineResponse2007Owner  # noqa: F401,E501


class InlineResponse2007(object):
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
        'default_workspace': 'InlineResponse2002DefaultWorkspace',
        'beta_capability_ids': 'list[str]',
        'public': 'bool',
        'owner': 'InlineResponse2007Owner',
        'permission_set': 'list[str]',
        'permission': 'str',
        'trashed_at': 'datetime',
        'trash': 'bool',
        'starred': 'str',
        'active': 'str',
        'created_at': 'datetime',
        'document_thumbnail_element_id': 'str',
        'thumbnail': 'InlineResponse2001Thumbnail',
        'created_by': 'InlineResponse2001CreatedBy',
        'modified_at': 'datetime',
        'modified_by': 'InlineResponse2001ModifiedBy',
        'tags': 'list[str]',
        'size_bytes': 'float',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'total_workspaces_updating': 'float',
        'total_workspaces_scheduled_for_update': 'float'
    }

    attribute_map = {
        'default_workspace': 'defaultWorkspace',
        'beta_capability_ids': 'betaCapabilityIds',
        'public': 'public',
        'owner': 'owner',
        'permission_set': 'permissionSet',
        'permission': 'permission',
        'trashed_at': 'trashedAt',
        'trash': 'trash',
        'starred': 'starred',
        'active': 'active',
        'created_at': 'createdAt',
        'document_thumbnail_element_id': 'documentThumbnailElementId',
        'thumbnail': 'thumbnail',
        'created_by': 'createdBy',
        'modified_at': 'modifiedAt',
        'modified_by': 'modifiedBy',
        'tags': 'tags',
        'size_bytes': 'sizeBytes',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'total_workspaces_updating': 'totalWorkspacesUpdating',
        'total_workspaces_scheduled_for_update': 'totalWorkspacesScheduledForUpdate'
    }

    def __init__(self, default_workspace=None, beta_capability_ids=None, public=None, owner=None, permission_set=None, permission=None, trashed_at=None, trash=None, starred=None, active=None, created_at=None, document_thumbnail_element_id=None, thumbnail=None, created_by=None, modified_at=None, modified_by=None, tags=None, size_bytes=None, name=None, id=None, href=None, total_workspaces_updating=None, total_workspaces_scheduled_for_update=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501

        self._default_workspace = None
        self._beta_capability_ids = None
        self._public = None
        self._owner = None
        self._permission_set = None
        self._permission = None
        self._trashed_at = None
        self._trash = None
        self._starred = None
        self._active = None
        self._created_at = None
        self._document_thumbnail_element_id = None
        self._thumbnail = None
        self._created_by = None
        self._modified_at = None
        self._modified_by = None
        self._tags = None
        self._size_bytes = None
        self._name = None
        self._id = None
        self._href = None
        self._total_workspaces_updating = None
        self._total_workspaces_scheduled_for_update = None
        self.discriminator = None

        self.default_workspace = default_workspace
        self.beta_capability_ids = beta_capability_ids
        self.public = public
        self.owner = owner
        self.permission_set = permission_set
        self.permission = permission
        self.trashed_at = trashed_at
        self.trash = trash
        self.starred = starred
        self.active = active
        self.created_at = created_at
        self.document_thumbnail_element_id = document_thumbnail_element_id
        self.thumbnail = thumbnail
        self.created_by = created_by
        self.modified_at = modified_at
        self.modified_by = modified_by
        self.tags = tags
        self.size_bytes = size_bytes
        self.name = name
        self.id = id
        self.href = href
        self.total_workspaces_updating = total_workspaces_updating
        self.total_workspaces_scheduled_for_update = total_workspaces_scheduled_for_update

    @property
    def default_workspace(self):
        """Gets the default_workspace of this InlineResponse2007.  # noqa: E501


        :return: The default_workspace of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2002DefaultWorkspace
        """
        return self._default_workspace

    @default_workspace.setter
    def default_workspace(self, default_workspace):
        """Sets the default_workspace of this InlineResponse2007.


        :param default_workspace: The default_workspace of this InlineResponse2007.  # noqa: E501
        :type: InlineResponse2002DefaultWorkspace
        """
        if default_workspace is None:
            raise ValueError("Invalid value for `default_workspace`, must not be `None`")  # noqa: E501

        self._default_workspace = default_workspace

    @property
    def beta_capability_ids(self):
        """Gets the beta_capability_ids of this InlineResponse2007.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The beta_capability_ids of this InlineResponse2007.  # noqa: E501
        :rtype: list[str]
        """
        return self._beta_capability_ids

    @beta_capability_ids.setter
    def beta_capability_ids(self, beta_capability_ids):
        """Sets the beta_capability_ids of this InlineResponse2007.

        Onshape internal use  # noqa: E501

        :param beta_capability_ids: The beta_capability_ids of this InlineResponse2007.  # noqa: E501
        :type: list[str]
        """
        if beta_capability_ids is None:
            raise ValueError("Invalid value for `beta_capability_ids`, must not be `None`")  # noqa: E501

        self._beta_capability_ids = beta_capability_ids

    @property
    def public(self):
        """Gets the public of this InlineResponse2007.  # noqa: E501

        Whether document is public  # noqa: E501

        :return: The public of this InlineResponse2007.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this InlineResponse2007.

        Whether document is public  # noqa: E501

        :param public: The public of this InlineResponse2007.  # noqa: E501
        :type: bool
        """
        if public is None:
            raise ValueError("Invalid value for `public`, must not be `None`")  # noqa: E501

        self._public = public

    @property
    def owner(self):
        """Gets the owner of this InlineResponse2007.  # noqa: E501


        :return: The owner of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2007Owner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InlineResponse2007.


        :param owner: The owner of this InlineResponse2007.  # noqa: E501
        :type: InlineResponse2007Owner
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def permission_set(self):
        """Gets the permission_set of this InlineResponse2007.  # noqa: E501

        User's level of access to the document. Possible values: OWNER,             DELETE, RESHARE, WRITE, READ, COPY, EXPORT, COMMENT  # noqa: E501

        :return: The permission_set of this InlineResponse2007.  # noqa: E501
        :rtype: list[str]
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this InlineResponse2007.

        User's level of access to the document. Possible values: OWNER,             DELETE, RESHARE, WRITE, READ, COPY, EXPORT, COMMENT  # noqa: E501

        :param permission_set: The permission_set of this InlineResponse2007.  # noqa: E501
        :type: list[str]
        """
        if permission_set is None:
            raise ValueError("Invalid value for `permission_set`, must not be `None`")  # noqa: E501

        self._permission_set = permission_set

    @property
    def permission(self):
        """Gets the permission of this InlineResponse2007.  # noqa: E501

        User's level of access to the document; can be ANONYMOUS_ACCESS, READ,             READ_COPY_EXPORT, COMMENT, WRITE, RESHARE, FULL, or OWNER (Deprecated)  # noqa: E501

        :return: The permission of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this InlineResponse2007.

        User's level of access to the document; can be ANONYMOUS_ACCESS, READ,             READ_COPY_EXPORT, COMMENT, WRITE, RESHARE, FULL, or OWNER (Deprecated)  # noqa: E501

        :param permission: The permission of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def trashed_at(self):
        """Gets the trashed_at of this InlineResponse2007.  # noqa: E501

        When document has been trashed  # noqa: E501

        :return: The trashed_at of this InlineResponse2007.  # noqa: E501
        :rtype: datetime
        """
        return self._trashed_at

    @trashed_at.setter
    def trashed_at(self, trashed_at):
        """Sets the trashed_at of this InlineResponse2007.

        When document has been trashed  # noqa: E501

        :param trashed_at: The trashed_at of this InlineResponse2007.  # noqa: E501
        :type: datetime
        """
        if trashed_at is None:
            raise ValueError("Invalid value for `trashed_at`, must not be `None`")  # noqa: E501

        self._trashed_at = trashed_at

    @property
    def trash(self):
        """Gets the trash of this InlineResponse2007.  # noqa: E501

        Whether document has been trashed  # noqa: E501

        :return: The trash of this InlineResponse2007.  # noqa: E501
        :rtype: bool
        """
        return self._trash

    @trash.setter
    def trash(self, trash):
        """Sets the trash of this InlineResponse2007.

        Whether document has been trashed  # noqa: E501

        :param trash: The trash of this InlineResponse2007.  # noqa: E501
        :type: bool
        """
        if trash is None:
            raise ValueError("Invalid value for `trash`, must not be `None`")  # noqa: E501

        self._trash = trash

    @property
    def starred(self):
        """Gets the starred of this InlineResponse2007.  # noqa: E501

        Whether document has been starred (Deprecated)  # noqa: E501

        :return: The starred of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this InlineResponse2007.

        Whether document has been starred (Deprecated)  # noqa: E501

        :param starred: The starred of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if starred is None:
            raise ValueError("Invalid value for `starred`, must not be `None`")  # noqa: E501

        self._starred = starred

    @property
    def active(self):
        """Gets the active of this InlineResponse2007.  # noqa: E501

        Whether a shared document is active  # noqa: E501

        :return: The active of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InlineResponse2007.

        Whether a shared document is active  # noqa: E501

        :param active: The active of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2007.  # noqa: E501

        Creation date  # noqa: E501

        :return: The created_at of this InlineResponse2007.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2007.

        Creation date  # noqa: E501

        :param created_at: The created_at of this InlineResponse2007.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def document_thumbnail_element_id(self):
        """Gets the document_thumbnail_element_id of this InlineResponse2007.  # noqa: E501

        The element which the Document Thumbnail should mirror  # noqa: E501

        :return: The document_thumbnail_element_id of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._document_thumbnail_element_id

    @document_thumbnail_element_id.setter
    def document_thumbnail_element_id(self, document_thumbnail_element_id):
        """Sets the document_thumbnail_element_id of this InlineResponse2007.

        The element which the Document Thumbnail should mirror  # noqa: E501

        :param document_thumbnail_element_id: The document_thumbnail_element_id of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if document_thumbnail_element_id is None:
            raise ValueError("Invalid value for `document_thumbnail_element_id`, must not be `None`")  # noqa: E501

        self._document_thumbnail_element_id = document_thumbnail_element_id

    @property
    def thumbnail(self):
        """Gets the thumbnail of this InlineResponse2007.  # noqa: E501


        :return: The thumbnail of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2001Thumbnail
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this InlineResponse2007.


        :param thumbnail: The thumbnail of this InlineResponse2007.  # noqa: E501
        :type: InlineResponse2001Thumbnail
        """
        if thumbnail is None:
            raise ValueError("Invalid value for `thumbnail`, must not be `None`")  # noqa: E501

        self._thumbnail = thumbnail

    @property
    def created_by(self):
        """Gets the created_by of this InlineResponse2007.  # noqa: E501


        :return: The created_by of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2001CreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InlineResponse2007.


        :param created_by: The created_by of this InlineResponse2007.  # noqa: E501
        :type: InlineResponse2001CreatedBy
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def modified_at(self):
        """Gets the modified_at of this InlineResponse2007.  # noqa: E501

        Date of last modification  # noqa: E501

        :return: The modified_at of this InlineResponse2007.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this InlineResponse2007.

        Date of last modification  # noqa: E501

        :param modified_at: The modified_at of this InlineResponse2007.  # noqa: E501
        :type: datetime
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this InlineResponse2007.  # noqa: E501


        :return: The modified_by of this InlineResponse2007.  # noqa: E501
        :rtype: InlineResponse2001ModifiedBy
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this InlineResponse2007.


        :param modified_by: The modified_by of this InlineResponse2007.  # noqa: E501
        :type: InlineResponse2001ModifiedBy
        """
        if modified_by is None:
            raise ValueError("Invalid value for `modified_by`, must not be `None`")  # noqa: E501

        self._modified_by = modified_by

    @property
    def tags(self):
        """Gets the tags of this InlineResponse2007.  # noqa: E501

        Reserved for future use  # noqa: E501

        :return: The tags of this InlineResponse2007.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineResponse2007.

        Reserved for future use  # noqa: E501

        :param tags: The tags of this InlineResponse2007.  # noqa: E501
        :type: list[str]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def size_bytes(self):
        """Gets the size_bytes of this InlineResponse2007.  # noqa: E501

        Size of document in bytes  # noqa: E501

        :return: The size_bytes of this InlineResponse2007.  # noqa: E501
        :rtype: float
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this InlineResponse2007.

        Size of document in bytes  # noqa: E501

        :param size_bytes: The size_bytes of this InlineResponse2007.  # noqa: E501
        :type: float
        """
        if size_bytes is None:
            raise ValueError("Invalid value for `size_bytes`, must not be `None`")  # noqa: E501

        self._size_bytes = size_bytes

    @property
    def name(self):
        """Gets the name of this InlineResponse2007.  # noqa: E501

        Name of document  # noqa: E501

        :return: The name of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2007.

        Name of document  # noqa: E501

        :param name: The name of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse2007.  # noqa: E501

        Document ID  # noqa: E501

        :return: The id of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2007.

        Document ID  # noqa: E501

        :param id: The id of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this InlineResponse2007.  # noqa: E501

        Document URL  # noqa: E501

        :return: The href of this InlineResponse2007.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this InlineResponse2007.

        Document URL  # noqa: E501

        :param href: The href of this InlineResponse2007.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def total_workspaces_updating(self):
        """Gets the total_workspaces_updating of this InlineResponse2007.  # noqa: E501

        Number of workspaces that are updating  # noqa: E501

        :return: The total_workspaces_updating of this InlineResponse2007.  # noqa: E501
        :rtype: float
        """
        return self._total_workspaces_updating

    @total_workspaces_updating.setter
    def total_workspaces_updating(self, total_workspaces_updating):
        """Sets the total_workspaces_updating of this InlineResponse2007.

        Number of workspaces that are updating  # noqa: E501

        :param total_workspaces_updating: The total_workspaces_updating of this InlineResponse2007.  # noqa: E501
        :type: float
        """
        if total_workspaces_updating is None:
            raise ValueError("Invalid value for `total_workspaces_updating`, must not be `None`")  # noqa: E501

        self._total_workspaces_updating = total_workspaces_updating

    @property
    def total_workspaces_scheduled_for_update(self):
        """Gets the total_workspaces_scheduled_for_update of this InlineResponse2007.  # noqa: E501

        Number of workspaces that are scheduled for             updating  # noqa: E501

        :return: The total_workspaces_scheduled_for_update of this InlineResponse2007.  # noqa: E501
        :rtype: float
        """
        return self._total_workspaces_scheduled_for_update

    @total_workspaces_scheduled_for_update.setter
    def total_workspaces_scheduled_for_update(self, total_workspaces_scheduled_for_update):
        """Sets the total_workspaces_scheduled_for_update of this InlineResponse2007.

        Number of workspaces that are scheduled for             updating  # noqa: E501

        :param total_workspaces_scheduled_for_update: The total_workspaces_scheduled_for_update of this InlineResponse2007.  # noqa: E501
        :type: float
        """
        if total_workspaces_scheduled_for_update is None:
            raise ValueError("Invalid value for `total_workspaces_scheduled_for_update`, must not be `None`")  # noqa: E501

        self._total_workspaces_scheduled_for_update = total_workspaces_scheduled_for_update

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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

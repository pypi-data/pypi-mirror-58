# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestResource(object):
    """
    A resource created, operated on or used by a work request.
    """

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "CREATED"
    ACTION_TYPE_CREATED = "CREATED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "UPDATED"
    ACTION_TYPE_UPDATED = "UPDATED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "DELETED"
    ACTION_TYPE_DELETED = "DELETED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "FAILED"
    ACTION_TYPE_FAILED = "FAILED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "IN_PROGRESS"
    ACTION_TYPE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "INSTALLED"
    ACTION_TYPE_INSTALLED = "INSTALLED"

    #: A constant which can be used with the action_type property of a WorkRequestResource.
    #: This constant has a value of "REMOVED"
    ACTION_TYPE_REMOVED = "REMOVED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this WorkRequestResource.
        :type entity_type: str

        :param action_type:
            The value to assign to the action_type property of this WorkRequestResource.
            Allowed values for this property are: "CREATED", "UPDATED", "DELETED", "FAILED", "IN_PROGRESS", "INSTALLED", "REMOVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_type: str

        :param identifier:
            The value to assign to the identifier property of this WorkRequestResource.
        :type identifier: str

        :param name:
            The value to assign to the name property of this WorkRequestResource.
        :type name: str

        :param entity_uri:
            The value to assign to the entity_uri property of this WorkRequestResource.
        :type entity_uri: str

        """
        self.swagger_types = {
            'entity_type': 'str',
            'action_type': 'str',
            'identifier': 'str',
            'name': 'str',
            'entity_uri': 'str'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'action_type': 'actionType',
            'identifier': 'identifier',
            'name': 'name',
            'entity_uri': 'entityUri'
        }

        self._entity_type = None
        self._action_type = None
        self._identifier = None
        self._name = None
        self._entity_uri = None

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this WorkRequestResource.
        The resource type for the work request.


        :return: The entity_type of this WorkRequestResource.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this WorkRequestResource.
        The resource type for the work request.


        :param entity_type: The entity_type of this WorkRequestResource.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this WorkRequestResource.
        The way in which this resource is affected by the work tracked in the work request.
        A resource being created, updated, or deleted will remain in the IN_PROGRESS state until
        work is complete for that resource at which point it will transition to CREATED, UPDATED,
        or DELETED, respectively. If the request failed for that resource,
        the state will be FAILED.

        Allowed values for this property are: "CREATED", "UPDATED", "DELETED", "FAILED", "IN_PROGRESS", "INSTALLED", "REMOVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_type of this WorkRequestResource.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this WorkRequestResource.
        The way in which this resource is affected by the work tracked in the work request.
        A resource being created, updated, or deleted will remain in the IN_PROGRESS state until
        work is complete for that resource at which point it will transition to CREATED, UPDATED,
        or DELETED, respectively. If the request failed for that resource,
        the state will be FAILED.


        :param action_type: The action_type of this WorkRequestResource.
        :type: str
        """
        allowed_values = ["CREATED", "UPDATED", "DELETED", "FAILED", "IN_PROGRESS", "INSTALLED", "REMOVED"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            action_type = 'UNKNOWN_ENUM_VALUE'
        self._action_type = action_type

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this WorkRequestResource.
        The identifier of the resource. Not all resources will have an id.


        :return: The identifier of this WorkRequestResource.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this WorkRequestResource.
        The identifier of the resource. Not all resources will have an id.


        :param identifier: The identifier of this WorkRequestResource.
        :type: str
        """
        self._identifier = identifier

    @property
    def name(self):
        """
        Gets the name of this WorkRequestResource.
        The name of the resource. Not all resources will have a name specified.


        :return: The name of this WorkRequestResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkRequestResource.
        The name of the resource. Not all resources will have a name specified.


        :param name: The name of this WorkRequestResource.
        :type: str
        """
        self._name = name

    @property
    def entity_uri(self):
        """
        **[Required]** Gets the entity_uri of this WorkRequestResource.
        The URI path that the user can do a GET on to access the resource metadata.


        :return: The entity_uri of this WorkRequestResource.
        :rtype: str
        """
        return self._entity_uri

    @entity_uri.setter
    def entity_uri(self, entity_uri):
        """
        Sets the entity_uri of this WorkRequestResource.
        The URI path that the user can do a GET on to access the resource metadata.


        :param entity_uri: The entity_uri of this WorkRequestResource.
        :type: str
        """
        self._entity_uri = entity_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

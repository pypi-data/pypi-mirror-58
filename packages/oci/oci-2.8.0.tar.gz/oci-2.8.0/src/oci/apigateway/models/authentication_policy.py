# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationPolicy(object):
    """
    Information on how to authenticate incoming requests.
    """

    #: A constant which can be used with the type property of a AuthenticationPolicy.
    #: This constant has a value of "CUSTOM_AUTHENTICATION"
    TYPE_CUSTOM_AUTHENTICATION = "CUSTOM_AUTHENTICATION"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.CustomAuthenticationPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_anonymous_access_allowed:
            The value to assign to the is_anonymous_access_allowed property of this AuthenticationPolicy.
        :type is_anonymous_access_allowed: bool

        :param type:
            The value to assign to the type property of this AuthenticationPolicy.
            Allowed values for this property are: "CUSTOM_AUTHENTICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'is_anonymous_access_allowed': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'is_anonymous_access_allowed': 'isAnonymousAccessAllowed',
            'type': 'type'
        }

        self._is_anonymous_access_allowed = None
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'CUSTOM_AUTHENTICATION':
            return 'CustomAuthenticationPolicy'
        else:
            return 'AuthenticationPolicy'

    @property
    def is_anonymous_access_allowed(self):
        """
        Gets the is_anonymous_access_allowed of this AuthenticationPolicy.
        Whether an unauthenticated user may access the API. Must be \"true\" to enable ANONYMOUS
        route authorization.


        :return: The is_anonymous_access_allowed of this AuthenticationPolicy.
        :rtype: bool
        """
        return self._is_anonymous_access_allowed

    @is_anonymous_access_allowed.setter
    def is_anonymous_access_allowed(self, is_anonymous_access_allowed):
        """
        Sets the is_anonymous_access_allowed of this AuthenticationPolicy.
        Whether an unauthenticated user may access the API. Must be \"true\" to enable ANONYMOUS
        route authorization.


        :param is_anonymous_access_allowed: The is_anonymous_access_allowed of this AuthenticationPolicy.
        :type: bool
        """
        self._is_anonymous_access_allowed = is_anonymous_access_allowed

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AuthenticationPolicy.
        Type of the authentication policy to use.

        Allowed values for this property are: "CUSTOM_AUTHENTICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AuthenticationPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AuthenticationPolicy.
        Type of the authentication policy to use.


        :param type: The type of this AuthenticationPolicy.
        :type: str
        """
        allowed_values = ["CUSTOM_AUTHENTICATION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

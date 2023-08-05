# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Hostname(object):
    """
    A hostname resource associated with a load balancer for use by one or more listeners.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Hostname object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Hostname.
        :type name: str

        :param hostname:
            The value to assign to the hostname property of this Hostname.
        :type hostname: str

        """
        self.swagger_types = {
            'name': 'str',
            'hostname': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'hostname': 'hostname'
        }

        self._name = None
        self._hostname = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Hostname.
        A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential
        information.

        Example: `example_hostname_001`


        :return: The name of this Hostname.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Hostname.
        A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential
        information.

        Example: `example_hostname_001`


        :param name: The name of this Hostname.
        :type: str
        """
        self._name = name

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this Hostname.
        A virtual hostname. For more information about virtual hostname string construction, see
        `Managing Request Routing`__.

        Example: `app.example.com`

        __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing


        :return: The hostname of this Hostname.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this Hostname.
        A virtual hostname. For more information about virtual hostname string construction, see
        `Managing Request Routing`__.

        Example: `app.example.com`

        __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing


        :param hostname: The hostname of this Hostname.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

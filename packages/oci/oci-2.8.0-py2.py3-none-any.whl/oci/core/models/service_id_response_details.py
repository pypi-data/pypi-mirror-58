# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ServiceIdResponseDetails(object):
    """
    ServiceIdResponseDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ServiceIdResponseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_id:
            The value to assign to the service_id property of this ServiceIdResponseDetails.
        :type service_id: str

        :param service_name:
            The value to assign to the service_name property of this ServiceIdResponseDetails.
        :type service_name: str

        """
        self.swagger_types = {
            'service_id': 'str',
            'service_name': 'str'
        }

        self.attribute_map = {
            'service_id': 'serviceId',
            'service_name': 'serviceName'
        }

        self._service_id = None
        self._service_name = None

    @property
    def service_id(self):
        """
        **[Required]** Gets the service_id of this ServiceIdResponseDetails.
        The `OCID`__ of the service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The service_id of this ServiceIdResponseDetails.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """
        Sets the service_id of this ServiceIdResponseDetails.
        The `OCID`__ of the service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param service_id: The service_id of this ServiceIdResponseDetails.
        :type: str
        """
        self._service_id = service_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this ServiceIdResponseDetails.
        The name of the service.


        :return: The service_name of this ServiceIdResponseDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this ServiceIdResponseDetails.
        The name of the service.


        :param service_name: The service_name of this ServiceIdResponseDetails.
        :type: str
        """
        self._service_name = service_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

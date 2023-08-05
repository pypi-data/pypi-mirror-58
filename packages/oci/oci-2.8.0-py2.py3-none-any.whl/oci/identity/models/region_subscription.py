# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RegionSubscription(object):
    """
    An object that represents your tenancy's access to a particular region (i.e., a subscription), the status of that
    access, and whether that region is the home region. For more information, see `Managing Regions`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Tasks/managingregions.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the status property of a RegionSubscription.
    #: This constant has a value of "READY"
    STATUS_READY = "READY"

    #: A constant which can be used with the status property of a RegionSubscription.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new RegionSubscription object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region_key:
            The value to assign to the region_key property of this RegionSubscription.
        :type region_key: str

        :param region_name:
            The value to assign to the region_name property of this RegionSubscription.
        :type region_name: str

        :param status:
            The value to assign to the status property of this RegionSubscription.
            Allowed values for this property are: "READY", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param is_home_region:
            The value to assign to the is_home_region property of this RegionSubscription.
        :type is_home_region: bool

        """
        self.swagger_types = {
            'region_key': 'str',
            'region_name': 'str',
            'status': 'str',
            'is_home_region': 'bool'
        }

        self.attribute_map = {
            'region_key': 'regionKey',
            'region_name': 'regionName',
            'status': 'status',
            'is_home_region': 'isHomeRegion'
        }

        self._region_key = None
        self._region_name = None
        self._status = None
        self._is_home_region = None

    @property
    def region_key(self):
        """
        **[Required]** Gets the region_key of this RegionSubscription.
        The region's key.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`
        - `LHR`
        - `YYZ`
        - `NRT`
        - `ICN`


        :return: The region_key of this RegionSubscription.
        :rtype: str
        """
        return self._region_key

    @region_key.setter
    def region_key(self, region_key):
        """
        Sets the region_key of this RegionSubscription.
        The region's key.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`
        - `LHR`
        - `YYZ`
        - `NRT`
        - `ICN`


        :param region_key: The region_key of this RegionSubscription.
        :type: str
        """
        self._region_key = region_key

    @property
    def region_name(self):
        """
        **[Required]** Gets the region_name of this RegionSubscription.
        The region's name.

        Allowed values are:
        - `ap-seoul-1`
        - `ap-tokyo-1`
        - `ca-toronto-1`
        - `eu-frankurt-1`
        - `uk-london-1`
        - `us-ashburn-1`
        - `us-phoenix-1`


        :return: The region_name of this RegionSubscription.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """
        Sets the region_name of this RegionSubscription.
        The region's name.

        Allowed values are:
        - `ap-seoul-1`
        - `ap-tokyo-1`
        - `ca-toronto-1`
        - `eu-frankurt-1`
        - `uk-london-1`
        - `us-ashburn-1`
        - `us-phoenix-1`


        :param region_name: The region_name of this RegionSubscription.
        :type: str
        """
        self._region_name = region_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this RegionSubscription.
        The region subscription status.

        Allowed values for this property are: "READY", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RegionSubscription.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RegionSubscription.
        The region subscription status.


        :param status: The status of this RegionSubscription.
        :type: str
        """
        allowed_values = ["READY", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def is_home_region(self):
        """
        **[Required]** Gets the is_home_region of this RegionSubscription.
        Indicates if the region is the home region or not.


        :return: The is_home_region of this RegionSubscription.
        :rtype: bool
        """
        return self._is_home_region

    @is_home_region.setter
    def is_home_region(self, is_home_region):
        """
        Sets the is_home_region of this RegionSubscription.
        Indicates if the region is the home region or not.


        :param is_home_region: The is_home_region of this RegionSubscription.
        :type: bool
        """
        self._is_home_region = is_home_region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

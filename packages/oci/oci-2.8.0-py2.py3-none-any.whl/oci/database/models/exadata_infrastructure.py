# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInfrastructure(object):
    """
    ExadataInfrastructure
    """

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "REQUIRES_ACTIVATION"
    LIFECYCLE_STATE_REQUIRES_ACTIVATION = "REQUIRES_ACTIVATION"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "ACTIVATING"
    LIFECYCLE_STATE_ACTIVATING = "ACTIVATING"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "ACTIVATION_FAILED"
    LIFECYCLE_STATE_ACTIVATION_FAILED = "ACTIVATION_FAILED"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExadataInfrastructure.
    #: This constant has a value of "OFFLINE"
    LIFECYCLE_STATE_OFFLINE = "OFFLINE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInfrastructure object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExadataInfrastructure.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExadataInfrastructure.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExadataInfrastructure.
            Allowed values for this property are: "CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this ExadataInfrastructure.
        :type display_name: str

        :param shape:
            The value to assign to the shape property of this ExadataInfrastructure.
        :type shape: str

        :param time_zone:
            The value to assign to the time_zone property of this ExadataInfrastructure.
        :type time_zone: str

        :param cpus_enabled:
            The value to assign to the cpus_enabled property of this ExadataInfrastructure.
        :type cpus_enabled: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this ExadataInfrastructure.
        :type data_storage_size_in_tbs: int

        :param cloud_control_plane_server1:
            The value to assign to the cloud_control_plane_server1 property of this ExadataInfrastructure.
        :type cloud_control_plane_server1: str

        :param cloud_control_plane_server2:
            The value to assign to the cloud_control_plane_server2 property of this ExadataInfrastructure.
        :type cloud_control_plane_server2: str

        :param netmask:
            The value to assign to the netmask property of this ExadataInfrastructure.
        :type netmask: str

        :param gateway:
            The value to assign to the gateway property of this ExadataInfrastructure.
        :type gateway: str

        :param admin_network_cidr:
            The value to assign to the admin_network_cidr property of this ExadataInfrastructure.
        :type admin_network_cidr: str

        :param infini_band_network_cidr:
            The value to assign to the infini_band_network_cidr property of this ExadataInfrastructure.
        :type infini_band_network_cidr: str

        :param corporate_proxy:
            The value to assign to the corporate_proxy property of this ExadataInfrastructure.
        :type corporate_proxy: str

        :param dns_server:
            The value to assign to the dns_server property of this ExadataInfrastructure.
        :type dns_server: list[str]

        :param ntp_server:
            The value to assign to the ntp_server property of this ExadataInfrastructure.
        :type ntp_server: list[str]

        :param time_created:
            The value to assign to the time_created property of this ExadataInfrastructure.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExadataInfrastructure.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExadataInfrastructure.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExadataInfrastructure.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'shape': 'str',
            'time_zone': 'str',
            'cpus_enabled': 'int',
            'data_storage_size_in_tbs': 'int',
            'cloud_control_plane_server1': 'str',
            'cloud_control_plane_server2': 'str',
            'netmask': 'str',
            'gateway': 'str',
            'admin_network_cidr': 'str',
            'infini_band_network_cidr': 'str',
            'corporate_proxy': 'str',
            'dns_server': 'list[str]',
            'ntp_server': 'list[str]',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'shape': 'shape',
            'time_zone': 'timeZone',
            'cpus_enabled': 'cpusEnabled',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'cloud_control_plane_server1': 'cloudControlPlaneServer1',
            'cloud_control_plane_server2': 'cloudControlPlaneServer2',
            'netmask': 'netmask',
            'gateway': 'gateway',
            'admin_network_cidr': 'adminNetworkCIDR',
            'infini_band_network_cidr': 'infiniBandNetworkCIDR',
            'corporate_proxy': 'corporateProxy',
            'dns_server': 'dnsServer',
            'ntp_server': 'ntpServer',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._display_name = None
        self._shape = None
        self._time_zone = None
        self._cpus_enabled = None
        self._data_storage_size_in_tbs = None
        self._cloud_control_plane_server1 = None
        self._cloud_control_plane_server2 = None
        self._netmask = None
        self._gateway = None
        self._admin_network_cidr = None
        self._infini_band_network_cidr = None
        self._corporate_proxy = None
        self._dns_server = None
        self._ntp_server = None
        self._time_created = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExadataInfrastructure.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExadataInfrastructure.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExadataInfrastructure.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExadataInfrastructure.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExadataInfrastructure.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExadataInfrastructure.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExadataInfrastructure.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExadataInfrastructure.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExadataInfrastructure.
        The current lifecycle state of the Exadata infrastructure.

        Allowed values for this property are: "CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExadataInfrastructure.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExadataInfrastructure.
        The current lifecycle state of the Exadata infrastructure.


        :param lifecycle_state: The lifecycle_state of this ExadataInfrastructure.
        :type: str
        """
        allowed_values = ["CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExadataInfrastructure.
        The user-friendly name for the Exadata infrastructure. The name does not need to be unique.


        :return: The display_name of this ExadataInfrastructure.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExadataInfrastructure.
        The user-friendly name for the Exadata infrastructure. The name does not need to be unique.


        :param display_name: The display_name of this ExadataInfrastructure.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this ExadataInfrastructure.
        The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.


        :return: The shape of this ExadataInfrastructure.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ExadataInfrastructure.
        The shape of the Exadata infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.


        :param shape: The shape of this ExadataInfrastructure.
        :type: str
        """
        self._shape = shape

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ExadataInfrastructure.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this ExadataInfrastructure.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ExadataInfrastructure.
        The time zone of the Exadata infrastructure. For details, see `Exadata Infrastructure Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this ExadataInfrastructure.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def cpus_enabled(self):
        """
        Gets the cpus_enabled of this ExadataInfrastructure.
        The number of enabled CPU cores.


        :return: The cpus_enabled of this ExadataInfrastructure.
        :rtype: int
        """
        return self._cpus_enabled

    @cpus_enabled.setter
    def cpus_enabled(self, cpus_enabled):
        """
        Sets the cpus_enabled of this ExadataInfrastructure.
        The number of enabled CPU cores.


        :param cpus_enabled: The cpus_enabled of this ExadataInfrastructure.
        :type: int
        """
        self._cpus_enabled = cpus_enabled

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this ExadataInfrastructure.
        Size, in terabytes, of the DATA disk group.


        :return: The data_storage_size_in_tbs of this ExadataInfrastructure.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this ExadataInfrastructure.
        Size, in terabytes, of the DATA disk group.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this ExadataInfrastructure.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def cloud_control_plane_server1(self):
        """
        Gets the cloud_control_plane_server1 of this ExadataInfrastructure.
        The IP address for the first control plane server.


        :return: The cloud_control_plane_server1 of this ExadataInfrastructure.
        :rtype: str
        """
        return self._cloud_control_plane_server1

    @cloud_control_plane_server1.setter
    def cloud_control_plane_server1(self, cloud_control_plane_server1):
        """
        Sets the cloud_control_plane_server1 of this ExadataInfrastructure.
        The IP address for the first control plane server.


        :param cloud_control_plane_server1: The cloud_control_plane_server1 of this ExadataInfrastructure.
        :type: str
        """
        self._cloud_control_plane_server1 = cloud_control_plane_server1

    @property
    def cloud_control_plane_server2(self):
        """
        Gets the cloud_control_plane_server2 of this ExadataInfrastructure.
        The IP address for the second control plane server.


        :return: The cloud_control_plane_server2 of this ExadataInfrastructure.
        :rtype: str
        """
        return self._cloud_control_plane_server2

    @cloud_control_plane_server2.setter
    def cloud_control_plane_server2(self, cloud_control_plane_server2):
        """
        Sets the cloud_control_plane_server2 of this ExadataInfrastructure.
        The IP address for the second control plane server.


        :param cloud_control_plane_server2: The cloud_control_plane_server2 of this ExadataInfrastructure.
        :type: str
        """
        self._cloud_control_plane_server2 = cloud_control_plane_server2

    @property
    def netmask(self):
        """
        Gets the netmask of this ExadataInfrastructure.
        The netmask for the control plane network.


        :return: The netmask of this ExadataInfrastructure.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """
        Sets the netmask of this ExadataInfrastructure.
        The netmask for the control plane network.


        :param netmask: The netmask of this ExadataInfrastructure.
        :type: str
        """
        self._netmask = netmask

    @property
    def gateway(self):
        """
        Gets the gateway of this ExadataInfrastructure.
        The gateway for the control plane network.


        :return: The gateway of this ExadataInfrastructure.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this ExadataInfrastructure.
        The gateway for the control plane network.


        :param gateway: The gateway of this ExadataInfrastructure.
        :type: str
        """
        self._gateway = gateway

    @property
    def admin_network_cidr(self):
        """
        Gets the admin_network_cidr of this ExadataInfrastructure.
        The CIDR block for the Exadata administration network.


        :return: The admin_network_cidr of this ExadataInfrastructure.
        :rtype: str
        """
        return self._admin_network_cidr

    @admin_network_cidr.setter
    def admin_network_cidr(self, admin_network_cidr):
        """
        Sets the admin_network_cidr of this ExadataInfrastructure.
        The CIDR block for the Exadata administration network.


        :param admin_network_cidr: The admin_network_cidr of this ExadataInfrastructure.
        :type: str
        """
        self._admin_network_cidr = admin_network_cidr

    @property
    def infini_band_network_cidr(self):
        """
        Gets the infini_band_network_cidr of this ExadataInfrastructure.
        The CIDR block for the Exadata InfiniBand interconnect.


        :return: The infini_band_network_cidr of this ExadataInfrastructure.
        :rtype: str
        """
        return self._infini_band_network_cidr

    @infini_band_network_cidr.setter
    def infini_band_network_cidr(self, infini_band_network_cidr):
        """
        Sets the infini_band_network_cidr of this ExadataInfrastructure.
        The CIDR block for the Exadata InfiniBand interconnect.


        :param infini_band_network_cidr: The infini_band_network_cidr of this ExadataInfrastructure.
        :type: str
        """
        self._infini_band_network_cidr = infini_band_network_cidr

    @property
    def corporate_proxy(self):
        """
        Gets the corporate_proxy of this ExadataInfrastructure.
        The corporate network proxy for access to the control plane network.


        :return: The corporate_proxy of this ExadataInfrastructure.
        :rtype: str
        """
        return self._corporate_proxy

    @corporate_proxy.setter
    def corporate_proxy(self, corporate_proxy):
        """
        Sets the corporate_proxy of this ExadataInfrastructure.
        The corporate network proxy for access to the control plane network.


        :param corporate_proxy: The corporate_proxy of this ExadataInfrastructure.
        :type: str
        """
        self._corporate_proxy = corporate_proxy

    @property
    def dns_server(self):
        """
        Gets the dns_server of this ExadataInfrastructure.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :return: The dns_server of this ExadataInfrastructure.
        :rtype: list[str]
        """
        return self._dns_server

    @dns_server.setter
    def dns_server(self, dns_server):
        """
        Sets the dns_server of this ExadataInfrastructure.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :param dns_server: The dns_server of this ExadataInfrastructure.
        :type: list[str]
        """
        self._dns_server = dns_server

    @property
    def ntp_server(self):
        """
        Gets the ntp_server of this ExadataInfrastructure.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :return: The ntp_server of this ExadataInfrastructure.
        :rtype: list[str]
        """
        return self._ntp_server

    @ntp_server.setter
    def ntp_server(self, ntp_server):
        """
        Sets the ntp_server of this ExadataInfrastructure.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :param ntp_server: The ntp_server of this ExadataInfrastructure.
        :type: list[str]
        """
        self._ntp_server = ntp_server

    @property
    def time_created(self):
        """
        Gets the time_created of this ExadataInfrastructure.
        The date and time the Exadata infrastructure was created.


        :return: The time_created of this ExadataInfrastructure.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExadataInfrastructure.
        The date and time the Exadata infrastructure was created.


        :param time_created: The time_created of this ExadataInfrastructure.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExadataInfrastructure.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExadataInfrastructure.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExadataInfrastructure.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExadataInfrastructure.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExadataInfrastructure.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExadataInfrastructure.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExadataInfrastructure.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExadataInfrastructure.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

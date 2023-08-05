# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityRule(object):
    """
    A security rule is one of the items in a :class:`NetworkSecurityGroup`.
    It is a virtual firewall rule for the VNICs in the network security group. A rule can be for
    either inbound (`direction`= INGRESS) or outbound (`direction`= EGRESS) IP packets.
    """

    #: A constant which can be used with the destination_type property of a SecurityRule.
    #: This constant has a value of "CIDR_BLOCK"
    DESTINATION_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the destination_type property of a SecurityRule.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    DESTINATION_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    #: A constant which can be used with the destination_type property of a SecurityRule.
    #: This constant has a value of "NETWORK_SECURITY_GROUP"
    DESTINATION_TYPE_NETWORK_SECURITY_GROUP = "NETWORK_SECURITY_GROUP"

    #: A constant which can be used with the direction property of a SecurityRule.
    #: This constant has a value of "EGRESS"
    DIRECTION_EGRESS = "EGRESS"

    #: A constant which can be used with the direction property of a SecurityRule.
    #: This constant has a value of "INGRESS"
    DIRECTION_INGRESS = "INGRESS"

    #: A constant which can be used with the source_type property of a SecurityRule.
    #: This constant has a value of "CIDR_BLOCK"
    SOURCE_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the source_type property of a SecurityRule.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    SOURCE_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    #: A constant which can be used with the source_type property of a SecurityRule.
    #: This constant has a value of "NETWORK_SECURITY_GROUP"
    SOURCE_TYPE_NETWORK_SECURITY_GROUP = "NETWORK_SECURITY_GROUP"

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this SecurityRule.
        :type description: str

        :param destination:
            The value to assign to the destination property of this SecurityRule.
        :type destination: str

        :param destination_type:
            The value to assign to the destination_type property of this SecurityRule.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type destination_type: str

        :param direction:
            The value to assign to the direction property of this SecurityRule.
            Allowed values for this property are: "EGRESS", "INGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type direction: str

        :param icmp_options:
            The value to assign to the icmp_options property of this SecurityRule.
        :type icmp_options: IcmpOptions

        :param id:
            The value to assign to the id property of this SecurityRule.
        :type id: str

        :param is_stateless:
            The value to assign to the is_stateless property of this SecurityRule.
        :type is_stateless: bool

        :param is_valid:
            The value to assign to the is_valid property of this SecurityRule.
        :type is_valid: bool

        :param protocol:
            The value to assign to the protocol property of this SecurityRule.
        :type protocol: str

        :param source:
            The value to assign to the source property of this SecurityRule.
        :type source: str

        :param source_type:
            The value to assign to the source_type property of this SecurityRule.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param tcp_options:
            The value to assign to the tcp_options property of this SecurityRule.
        :type tcp_options: TcpOptions

        :param time_created:
            The value to assign to the time_created property of this SecurityRule.
        :type time_created: datetime

        :param udp_options:
            The value to assign to the udp_options property of this SecurityRule.
        :type udp_options: UdpOptions

        """
        self.swagger_types = {
            'description': 'str',
            'destination': 'str',
            'destination_type': 'str',
            'direction': 'str',
            'icmp_options': 'IcmpOptions',
            'id': 'str',
            'is_stateless': 'bool',
            'is_valid': 'bool',
            'protocol': 'str',
            'source': 'str',
            'source_type': 'str',
            'tcp_options': 'TcpOptions',
            'time_created': 'datetime',
            'udp_options': 'UdpOptions'
        }

        self.attribute_map = {
            'description': 'description',
            'destination': 'destination',
            'destination_type': 'destinationType',
            'direction': 'direction',
            'icmp_options': 'icmpOptions',
            'id': 'id',
            'is_stateless': 'isStateless',
            'is_valid': 'isValid',
            'protocol': 'protocol',
            'source': 'source',
            'source_type': 'sourceType',
            'tcp_options': 'tcpOptions',
            'time_created': 'timeCreated',
            'udp_options': 'udpOptions'
        }

        self._description = None
        self._destination = None
        self._destination_type = None
        self._direction = None
        self._icmp_options = None
        self._id = None
        self._is_stateless = None
        self._is_valid = None
        self._protocol = None
        self._source = None
        self._source_type = None
        self._tcp_options = None
        self._time_created = None
        self._udp_options = None

    @property
    def description(self):
        """
        Gets the description of this SecurityRule.
        An optional description of your choice for the rule.


        :return: The description of this SecurityRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityRule.
        An optional description of your choice for the rule.


        :param description: The description of this SecurityRule.
        :type: str
        """
        self._description = description

    @property
    def destination(self):
        """
        Gets the destination of this SecurityRule.
        Conceptually, this is the range of IP addresses that a packet originating from the instance
        can go to.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in the Government Cloud.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.


        :return: The destination of this SecurityRule.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this SecurityRule.
        Conceptually, this is the range of IP addresses that a packet originating from the instance
        can go to.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in the Government Cloud.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.


        :param destination: The destination of this SecurityRule.
        :type: str
        """
        self._destination = destination

    @property
    def destination_type(self):
        """
        Gets the destination_type of this SecurityRule.
        Type of destination for the rule. Required if `direction` = `EGRESS`.

        Allowed values:

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the OCID of a
            :class:`NetworkSecurityGroup`.

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The destination_type of this SecurityRule.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this SecurityRule.
        Type of destination for the rule. Required if `direction` = `EGRESS`.

        Allowed values:

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the OCID of a
            :class:`NetworkSecurityGroup`.


        :param destination_type: The destination_type of this SecurityRule.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"]
        if not value_allowed_none_or_none_sentinel(destination_type, allowed_values):
            destination_type = 'UNKNOWN_ENUM_VALUE'
        self._destination_type = destination_type

    @property
    def direction(self):
        """
        **[Required]** Gets the direction of this SecurityRule.
        Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.

        Allowed values for this property are: "EGRESS", "INGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The direction of this SecurityRule.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this SecurityRule.
        Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.


        :param direction: The direction of this SecurityRule.
        :type: str
        """
        allowed_values = ["EGRESS", "INGRESS"]
        if not value_allowed_none_or_none_sentinel(direction, allowed_values):
            direction = 'UNKNOWN_ENUM_VALUE'
        self._direction = direction

    @property
    def icmp_options(self):
        """
        Gets the icmp_options of this SecurityRule.
        Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code
        as defined in:
        - `ICMP Parameters`__
        - `ICMPv6 Parameters`__

        If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security rule for each.

        __ http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml
        __ https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml


        :return: The icmp_options of this SecurityRule.
        :rtype: IcmpOptions
        """
        return self._icmp_options

    @icmp_options.setter
    def icmp_options(self, icmp_options):
        """
        Sets the icmp_options of this SecurityRule.
        Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code
        as defined in:
        - `ICMP Parameters`__
        - `ICMPv6 Parameters`__

        If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security rule for each.

        __ http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml
        __ https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml


        :param icmp_options: The icmp_options of this SecurityRule.
        :type: IcmpOptions
        """
        self._icmp_options = icmp_options

    @property
    def id(self):
        """
        Gets the id of this SecurityRule.
        An Oracle-assigned identifier for the security rule. You specify this ID when you want to
        update or delete the rule.

        Example: `04ABEC`


        :return: The id of this SecurityRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityRule.
        An Oracle-assigned identifier for the security rule. You specify this ID when you want to
        update or delete the rule.

        Example: `04ABEC`


        :param id: The id of this SecurityRule.
        :type: str
        """
        self._id = id

    @property
    def is_stateless(self):
        """
        Gets the is_stateless of this SecurityRule.
        A stateless rule allows traffic in one direction. Remember to add a corresponding
        stateless rule in the other direction if you need to support bidirectional traffic. For
        example, if egress traffic allows TCP destination port 80, there should be an ingress
        rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
        and a corresponding rule is not necessary for bidirectional traffic.


        :return: The is_stateless of this SecurityRule.
        :rtype: bool
        """
        return self._is_stateless

    @is_stateless.setter
    def is_stateless(self, is_stateless):
        """
        Sets the is_stateless of this SecurityRule.
        A stateless rule allows traffic in one direction. Remember to add a corresponding
        stateless rule in the other direction if you need to support bidirectional traffic. For
        example, if egress traffic allows TCP destination port 80, there should be an ingress
        rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
        and a corresponding rule is not necessary for bidirectional traffic.


        :param is_stateless: The is_stateless of this SecurityRule.
        :type: bool
        """
        self._is_stateless = is_stateless

    @property
    def is_valid(self):
        """
        Gets the is_valid of this SecurityRule.
        Whether the rule is valid. The value is `True` when the rule is first created. If
        the rule's `source` or `destination` is a network security group, the value changes to
        `False` if that network security group is deleted.


        :return: The is_valid of this SecurityRule.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """
        Sets the is_valid of this SecurityRule.
        Whether the rule is valid. The value is `True` when the rule is first created. If
        the rule's `source` or `destination` is a network security group, the value changes to
        `False` if that network security group is deleted.


        :param is_valid: The is_valid of this SecurityRule.
        :type: bool
        """
        self._is_valid = is_valid

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this SecurityRule.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        `Protocol Numbers`__.
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

        __ http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml


        :return: The protocol of this SecurityRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this SecurityRule.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        `Protocol Numbers`__.
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

        __ http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml


        :param protocol: The protocol of this SecurityRule.
        :type: str
        """
        self._protocol = protocol

    @property
    def source(self):
        """
        Gets the source of this SecurityRule.
        Conceptually, this is the range of IP addresses that a packet coming into the instance
        can come from.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in the Government Cloud.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic coming from a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.


        :return: The source of this SecurityRule.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this SecurityRule.
        Conceptually, this is the range of IP addresses that a packet coming into the instance
        can come from.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in the Government Cloud.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic coming from a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.


        :param source: The source of this SecurityRule.
        :type: str
        """
        self._source = source

    @property
    def source_type(self):
        """
        Gets the source_type of this SecurityRule.
        Type of source for the rule. Required if `direction` = `INGRESS`.

          * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic coming from a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the OCID of a
            :class:`NetworkSecurityGroup`.

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this SecurityRule.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this SecurityRule.
        Type of source for the rule. Required if `direction` = `INGRESS`.

          * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic coming from a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the OCID of a
            :class:`NetworkSecurityGroup`.


        :param source_type: The source_type of this SecurityRule.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def tcp_options(self):
        """
        Gets the tcp_options of this SecurityRule.
        Optional and valid only for TCP. Use to specify particular destination ports for TCP rules.
        If you specify TCP as the protocol but omit this object, then all destination ports are allowed.


        :return: The tcp_options of this SecurityRule.
        :rtype: TcpOptions
        """
        return self._tcp_options

    @tcp_options.setter
    def tcp_options(self, tcp_options):
        """
        Sets the tcp_options of this SecurityRule.
        Optional and valid only for TCP. Use to specify particular destination ports for TCP rules.
        If you specify TCP as the protocol but omit this object, then all destination ports are allowed.


        :param tcp_options: The tcp_options of this SecurityRule.
        :type: TcpOptions
        """
        self._tcp_options = tcp_options

    @property
    def time_created(self):
        """
        Gets the time_created of this SecurityRule.
        The date and time the security rule was created. Format defined by RFC3339.


        :return: The time_created of this SecurityRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityRule.
        The date and time the security rule was created. Format defined by RFC3339.


        :param time_created: The time_created of this SecurityRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def udp_options(self):
        """
        Gets the udp_options of this SecurityRule.
        Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
        If you specify UDP as the protocol but omit this object, then all destination ports are allowed.


        :return: The udp_options of this SecurityRule.
        :rtype: UdpOptions
        """
        return self._udp_options

    @udp_options.setter
    def udp_options(self, udp_options):
        """
        Sets the udp_options of this SecurityRule.
        Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
        If you specify UDP as the protocol but omit this object, then all destination ports are allowed.


        :param udp_options: The udp_options of this SecurityRule.
        :type: UdpOptions
        """
        self._udp_options = udp_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

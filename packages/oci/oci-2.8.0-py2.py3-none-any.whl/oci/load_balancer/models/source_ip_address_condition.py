# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .rule_condition import RuleCondition
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceIpAddressCondition(RuleCondition):
    """
    An access control rule condition that requires a match on the specified source IP address or address range.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SourceIpAddressCondition object with values from keyword arguments. The default value of the :py:attr:`~oci.load_balancer.models.SourceIpAddressCondition.attribute_name` attribute
        of this class is ``SOURCE_IP_ADDRESS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attribute_name:
            The value to assign to the attribute_name property of this SourceIpAddressCondition.
            Allowed values for this property are: "SOURCE_IP_ADDRESS", "SOURCE_VCN_ID", "SOURCE_VCN_IP_ADDRESS", "PATH"
        :type attribute_name: str

        :param attribute_value:
            The value to assign to the attribute_value property of this SourceIpAddressCondition.
        :type attribute_value: str

        """
        self.swagger_types = {
            'attribute_name': 'str',
            'attribute_value': 'str'
        }

        self.attribute_map = {
            'attribute_name': 'attributeName',
            'attribute_value': 'attributeValue'
        }

        self._attribute_name = None
        self._attribute_value = None
        self._attribute_name = 'SOURCE_IP_ADDRESS'

    @property
    def attribute_value(self):
        """
        **[Required]** Gets the attribute_value of this SourceIpAddressCondition.
        An IPv4 or IPv6 address range that the source IP address of an incoming packet must match.

        The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y or x:x::x/y) strings.

        Specify 0.0.0.0/0 or ::/0 to match all incoming traffic.


        :return: The attribute_value of this SourceIpAddressCondition.
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """
        Sets the attribute_value of this SourceIpAddressCondition.
        An IPv4 or IPv6 address range that the source IP address of an incoming packet must match.

        The service accepts only classless inter-domain routing (CIDR) format (x.x.x.x/y or x:x::x/y) strings.

        Specify 0.0.0.0/0 or ::/0 to match all incoming traffic.


        :param attribute_value: The attribute_value of this SourceIpAddressCondition.
        :type: str
        """
        self._attribute_value = attribute_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

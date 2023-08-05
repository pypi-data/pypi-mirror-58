# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOdaInstanceDetails(object):
    """
    The Digital Assistant instance information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOdaInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateOdaInstanceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateOdaInstanceDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOdaInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOdaInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateOdaInstanceDetails.
        User-friendly name for the Digital Assistant instance.


        :return: The display_name of this UpdateOdaInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateOdaInstanceDetails.
        User-friendly name for the Digital Assistant instance.


        :param display_name: The display_name of this UpdateOdaInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateOdaInstanceDetails.
        Description of the Digital Assistant instance.


        :return: The description of this UpdateOdaInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateOdaInstanceDetails.
        Description of the Digital Assistant instance.


        :param description: The description of this UpdateOdaInstanceDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOdaInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for
        cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOdaInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOdaInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for
        cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOdaInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOdaInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOdaInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOdaInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOdaInstanceDetails.
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

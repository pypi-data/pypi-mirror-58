# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVolumeBackupPolicyDetails(object):
    """
    Specifies the properties for creating user defined backup policy.
    For more information about user defined backup policies,
    see `User Defined Policies`__ in
    `Policy-Based Backups`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#UserDefinedBackupPolicies
    __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVolumeBackupPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVolumeBackupPolicyDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateVolumeBackupPolicyDetails.
        :type display_name: str

        :param schedules:
            The value to assign to the schedules property of this CreateVolumeBackupPolicyDetails.
        :type schedules: list[VolumeBackupSchedule]

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVolumeBackupPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVolumeBackupPolicyDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'schedules': 'list[VolumeBackupSchedule]',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'schedules': 'schedules',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._schedules = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVolumeBackupPolicyDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateVolumeBackupPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVolumeBackupPolicyDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateVolumeBackupPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVolumeBackupPolicyDetails.
        A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateVolumeBackupPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVolumeBackupPolicyDetails.
        A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVolumeBackupPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def schedules(self):
        """
        Gets the schedules of this CreateVolumeBackupPolicyDetails.
        The collection of schedules for the volume backup policy. See
        see `Schedules`__ in
        `Policy-Based Backups`__ for more information.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#schedules
        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm


        :return: The schedules of this CreateVolumeBackupPolicyDetails.
        :rtype: list[VolumeBackupSchedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this CreateVolumeBackupPolicyDetails.
        The collection of schedules for the volume backup policy. See
        see `Schedules`__ in
        `Policy-Based Backups`__ for more information.

        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#schedules
        __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm


        :param schedules: The schedules of this CreateVolumeBackupPolicyDetails.
        :type: list[VolumeBackupSchedule]
        """
        self._schedules = schedules

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVolumeBackupPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVolumeBackupPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVolumeBackupPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVolumeBackupPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVolumeBackupPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVolumeBackupPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVolumeBackupPolicyDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVolumeBackupPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

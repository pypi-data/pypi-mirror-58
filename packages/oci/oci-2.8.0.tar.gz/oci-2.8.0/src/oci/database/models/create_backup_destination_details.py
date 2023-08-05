# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBackupDestinationDetails(object):
    """
    Details for creating a backup destination.
    """

    #: A constant which can be used with the type property of a CreateBackupDestinationDetails.
    #: This constant has a value of "NFS"
    TYPE_NFS = "NFS"

    #: A constant which can be used with the type property of a CreateBackupDestinationDetails.
    #: This constant has a value of "RECOVERY_APPLIANCE"
    TYPE_RECOVERY_APPLIANCE = "RECOVERY_APPLIANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBackupDestinationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateNFSBackupDestinationDetails`
        * :class:`~oci.database.models.CreateRecoveryApplianceBackupDestinationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateBackupDestinationDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateBackupDestinationDetails.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this CreateBackupDestinationDetails.
            Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE"
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBackupDestinationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBackupDestinationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'NFS':
            return 'CreateNFSBackupDestinationDetails'

        if type == 'RECOVERY_APPLIANCE':
            return 'CreateRecoveryApplianceBackupDestinationDetails'
        else:
            return 'CreateBackupDestinationDetails'

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateBackupDestinationDetails.
        The user-provided name of the backup destination.


        :return: The display_name of this CreateBackupDestinationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBackupDestinationDetails.
        The user-provided name of the backup destination.


        :param display_name: The display_name of this CreateBackupDestinationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateBackupDestinationDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateBackupDestinationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateBackupDestinationDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateBackupDestinationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateBackupDestinationDetails.
        Type of the backup destination.

        Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE"


        :return: The type of this CreateBackupDestinationDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateBackupDestinationDetails.
        Type of the backup destination.


        :param type: The type of this CreateBackupDestinationDetails.
        :type: str
        """
        allowed_values = ["NFS", "RECOVERY_APPLIANCE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBackupDestinationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateBackupDestinationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBackupDestinationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateBackupDestinationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBackupDestinationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateBackupDestinationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBackupDestinationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateBackupDestinationDetails.
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

# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .boot_volume_source_details import BootVolumeSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolumeSourceFromBootVolumeDetails(BootVolumeSourceDetails):
    """
    Specifies the source boot volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolumeSourceFromBootVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.BootVolumeSourceFromBootVolumeDetails.type` attribute
        of this class is ``bootVolume`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this BootVolumeSourceFromBootVolumeDetails.
        :type type: str

        :param id:
            The value to assign to the id property of this BootVolumeSourceFromBootVolumeDetails.
        :type id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None
        self._type = 'bootVolume'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BootVolumeSourceFromBootVolumeDetails.
        The OCID of the boot volume.


        :return: The id of this BootVolumeSourceFromBootVolumeDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BootVolumeSourceFromBootVolumeDetails.
        The OCID of the boot volume.


        :param id: The id of this BootVolumeSourceFromBootVolumeDetails.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

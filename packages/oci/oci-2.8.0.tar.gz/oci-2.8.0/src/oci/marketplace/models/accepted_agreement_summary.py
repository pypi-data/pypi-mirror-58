# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AcceptedAgreementSummary(object):
    """
    The model for a summary of an accepted agreement.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AcceptedAgreementSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AcceptedAgreementSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this AcceptedAgreementSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AcceptedAgreementSummary.
        :type compartment_id: str

        :param listing_id:
            The value to assign to the listing_id property of this AcceptedAgreementSummary.
        :type listing_id: str

        :param package_version:
            The value to assign to the package_version property of this AcceptedAgreementSummary.
        :type package_version: str

        :param agreement_id:
            The value to assign to the agreement_id property of this AcceptedAgreementSummary.
        :type agreement_id: str

        :param time_accepted:
            The value to assign to the time_accepted property of this AcceptedAgreementSummary.
        :type time_accepted: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'listing_id': 'str',
            'package_version': 'str',
            'agreement_id': 'str',
            'time_accepted': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'listing_id': 'listingId',
            'package_version': 'packageVersion',
            'agreement_id': 'agreementId',
            'time_accepted': 'timeAccepted'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._listing_id = None
        self._package_version = None
        self._agreement_id = None
        self._time_accepted = None

    @property
    def id(self):
        """
        Gets the id of this AcceptedAgreementSummary.
        The unique identifier for the acceptance of the agreement within a specific compartment.


        :return: The id of this AcceptedAgreementSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AcceptedAgreementSummary.
        The unique identifier for the acceptance of the agreement within a specific compartment.


        :param id: The id of this AcceptedAgreementSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this AcceptedAgreementSummary.
        A display name for the accepted agreement.


        :return: The display_name of this AcceptedAgreementSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AcceptedAgreementSummary.
        A display name for the accepted agreement.


        :param display_name: The display_name of this AcceptedAgreementSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AcceptedAgreementSummary.
        The unique identifier for the compartment where the agreement was accepted.


        :return: The compartment_id of this AcceptedAgreementSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AcceptedAgreementSummary.
        The unique identifier for the compartment where the agreement was accepted.


        :param compartment_id: The compartment_id of this AcceptedAgreementSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def listing_id(self):
        """
        Gets the listing_id of this AcceptedAgreementSummary.
        The unique identifier for the listing associated with the agreement.


        :return: The listing_id of this AcceptedAgreementSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this AcceptedAgreementSummary.
        The unique identifier for the listing associated with the agreement.


        :param listing_id: The listing_id of this AcceptedAgreementSummary.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def package_version(self):
        """
        Gets the package_version of this AcceptedAgreementSummary.
        The package version associated with the agreement.


        :return: The package_version of this AcceptedAgreementSummary.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this AcceptedAgreementSummary.
        The package version associated with the agreement.


        :param package_version: The package_version of this AcceptedAgreementSummary.
        :type: str
        """
        self._package_version = package_version

    @property
    def agreement_id(self):
        """
        Gets the agreement_id of this AcceptedAgreementSummary.
        The unique identifier for the terms of use agreement itself.


        :return: The agreement_id of this AcceptedAgreementSummary.
        :rtype: str
        """
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, agreement_id):
        """
        Sets the agreement_id of this AcceptedAgreementSummary.
        The unique identifier for the terms of use agreement itself.


        :param agreement_id: The agreement_id of this AcceptedAgreementSummary.
        :type: str
        """
        self._agreement_id = agreement_id

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this AcceptedAgreementSummary.
        The time the agreement was accepted.


        :return: The time_accepted of this AcceptedAgreementSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this AcceptedAgreementSummary.
        The time the agreement was accepted.


        :param time_accepted: The time_accepted of this AcceptedAgreementSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

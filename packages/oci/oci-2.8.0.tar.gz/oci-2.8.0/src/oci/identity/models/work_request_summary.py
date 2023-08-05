# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    The work request summary. Tracks the status of the asynchronous operation.
    """

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_COMPARTMENT"
    OPERATION_TYPE_DELETE_COMPARTMENT = "DELETE_COMPARTMENT"

    #: A constant which can be used with the operation_type property of a WorkRequestSummary.
    #: This constant has a value of "DELETE_TAG_DEFINITION"
    OPERATION_TYPE_DELETE_TAG_DEFINITION = "DELETE_TAG_DEFINITION"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequestSummary.
            Allowed values for this property are: "DELETE_COMPARTMENT", "DELETE_TAG_DEFINITION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param resources:
            The value to assign to the resources property of this WorkRequestSummary.
        :type resources: list[WorkRequestResource]

        :param errors:
            The value to assign to the errors property of this WorkRequestSummary.
        :type errors: list[WorkRequestError]

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: float

        """
        self.swagger_types = {
            'id': 'str',
            'operation_type': 'str',
            'compartment_id': 'str',
            'status': 'str',
            'resources': 'list[WorkRequestResource]',
            'errors': 'list[WorkRequestError]',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'percent_complete': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'operation_type': 'operationType',
            'compartment_id': 'compartmentId',
            'status': 'status',
            'resources': 'resources',
            'errors': 'errors',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'percent_complete': 'percentComplete'
        }

        self._id = None
        self._operation_type = None
        self._compartment_id = None
        self._status = None
        self._resources = None
        self._errors = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._percent_complete = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        The OCID of the work request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        The OCID of the work request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequestSummary.
        An enum-like description of the type of work the work request is doing.

        Allowed values for this property are: "DELETE_COMPARTMENT", "DELETE_TAG_DEFINITION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequestSummary.
        An enum-like description of the type of work the work request is doing.


        :param operation_type: The operation_type of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["DELETE_COMPARTMENT", "DELETE_TAG_DEFINITION"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequestSummary.
        The current status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        The current status of the work request.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def resources(self):
        """
        Gets the resources of this WorkRequestSummary.
        The resources this work request affects.


        :return: The resources of this WorkRequestSummary.
        :rtype: list[WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequestSummary.
        The resources this work request affects.


        :param resources: The resources of this WorkRequestSummary.
        :type: list[WorkRequestResource]
        """
        self._resources = resources

    @property
    def errors(self):
        """
        Gets the errors of this WorkRequestSummary.
        The errors for work request.


        :return: The errors of this WorkRequestSummary.
        :rtype: list[WorkRequestError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this WorkRequestSummary.
        The errors for work request.


        :param errors: The errors of this WorkRequestSummary.
        :type: list[WorkRequestError]
        """
        self._errors = errors

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this WorkRequestSummary.
        Date and time the work was accepted, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        Date and time the work was accepted, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequestSummary.
        Date and time the work started, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        Date and time the work started, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        Date and time the work completed, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        Date and time the work completed, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this WorkRequestSummary.
        How much progress the operation has made.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        How much progress the operation has made.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

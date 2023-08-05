# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledJob(object):
    """
    Detailed information about a Scheduled Job
    """

    #: A constant which can be used with the schedule_type property of a ScheduledJob.
    #: This constant has a value of "ONETIME"
    SCHEDULE_TYPE_ONETIME = "ONETIME"

    #: A constant which can be used with the schedule_type property of a ScheduledJob.
    #: This constant has a value of "RECURRING"
    SCHEDULE_TYPE_RECURRING = "RECURRING"

    #: A constant which can be used with the interval_type property of a ScheduledJob.
    #: This constant has a value of "HOUR"
    INTERVAL_TYPE_HOUR = "HOUR"

    #: A constant which can be used with the interval_type property of a ScheduledJob.
    #: This constant has a value of "DAY"
    INTERVAL_TYPE_DAY = "DAY"

    #: A constant which can be used with the interval_type property of a ScheduledJob.
    #: This constant has a value of "WEEK"
    INTERVAL_TYPE_WEEK = "WEEK"

    #: A constant which can be used with the interval_type property of a ScheduledJob.
    #: This constant has a value of "MONTH"
    INTERVAL_TYPE_MONTH = "MONTH"

    #: A constant which can be used with the operation_type property of a ScheduledJob.
    #: This constant has a value of "INSTALL"
    OPERATION_TYPE_INSTALL = "INSTALL"

    #: A constant which can be used with the operation_type property of a ScheduledJob.
    #: This constant has a value of "UPDATE"
    OPERATION_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the operation_type property of a ScheduledJob.
    #: This constant has a value of "REMOVE"
    OPERATION_TYPE_REMOVE = "REMOVE"

    #: A constant which can be used with the operation_type property of a ScheduledJob.
    #: This constant has a value of "UPDATEALL"
    OPERATION_TYPE_UPDATEALL = "UPDATEALL"

    #: A constant which can be used with the update_type property of a ScheduledJob.
    #: This constant has a value of "SECURITY"
    UPDATE_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the update_type property of a ScheduledJob.
    #: This constant has a value of "BUGFIX"
    UPDATE_TYPE_BUGFIX = "BUGFIX"

    #: A constant which can be used with the update_type property of a ScheduledJob.
    #: This constant has a value of "ENHANCEMENT"
    UPDATE_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the update_type property of a ScheduledJob.
    #: This constant has a value of "ALL"
    UPDATE_TYPE_ALL = "ALL"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJob.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJob.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJob.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJob.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJob.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ScheduledJob.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ScheduledJob.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduledJob.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledJob.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ScheduledJob.
        :type description: str

        :param schedule_type:
            The value to assign to the schedule_type property of this ScheduledJob.
            Allowed values for this property are: "ONETIME", "RECURRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schedule_type: str

        :param time_next_execution:
            The value to assign to the time_next_execution property of this ScheduledJob.
        :type time_next_execution: datetime

        :param time_last_execution:
            The value to assign to the time_last_execution property of this ScheduledJob.
        :type time_last_execution: datetime

        :param interval_type:
            The value to assign to the interval_type property of this ScheduledJob.
            Allowed values for this property are: "HOUR", "DAY", "WEEK", "MONTH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type interval_type: str

        :param interval_value:
            The value to assign to the interval_value property of this ScheduledJob.
        :type interval_value: str

        :param managed_instances:
            The value to assign to the managed_instances property of this ScheduledJob.
        :type managed_instances: list[Id]

        :param managed_instance_groups:
            The value to assign to the managed_instance_groups property of this ScheduledJob.
        :type managed_instance_groups: list[Id]

        :param operation_type:
            The value to assign to the operation_type property of this ScheduledJob.
            Allowed values for this property are: "INSTALL", "UPDATE", "REMOVE", "UPDATEALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param update_type:
            The value to assign to the update_type property of this ScheduledJob.
            Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type update_type: str

        :param package_names:
            The value to assign to the package_names property of this ScheduledJob.
        :type package_names: list[PackageName]

        :param work_requests:
            The value to assign to the work_requests property of this ScheduledJob.
        :type work_requests: list[Id]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledJob.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduledJob.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduledJob.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'schedule_type': 'str',
            'time_next_execution': 'datetime',
            'time_last_execution': 'datetime',
            'interval_type': 'str',
            'interval_value': 'str',
            'managed_instances': 'list[Id]',
            'managed_instance_groups': 'list[Id]',
            'operation_type': 'str',
            'update_type': 'str',
            'package_names': 'list[PackageName]',
            'work_requests': 'list[Id]',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'schedule_type': 'scheduleType',
            'time_next_execution': 'timeNextExecution',
            'time_last_execution': 'timeLastExecution',
            'interval_type': 'intervalType',
            'interval_value': 'intervalValue',
            'managed_instances': 'managedInstances',
            'managed_instance_groups': 'managedInstanceGroups',
            'operation_type': 'operationType',
            'update_type': 'updateType',
            'package_names': 'packageNames',
            'work_requests': 'workRequests',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._schedule_type = None
        self._time_next_execution = None
        self._time_last_execution = None
        self._interval_type = None
        self._interval_value = None
        self._managed_instances = None
        self._managed_instance_groups = None
        self._operation_type = None
        self._update_type = None
        self._package_names = None
        self._work_requests = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledJob.
        OCID for the Scheduled Job


        :return: The id of this ScheduledJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledJob.
        OCID for the Scheduled Job


        :param id: The id of this ScheduledJob.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this ScheduledJob.
        OCID for the Compartment


        :return: The compartment_id of this ScheduledJob.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduledJob.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this ScheduledJob.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduledJob.
        Scheduled Job name


        :return: The display_name of this ScheduledJob.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduledJob.
        Scheduled Job name


        :param display_name: The display_name of this ScheduledJob.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ScheduledJob.
        Details describing the Scheduled Job.


        :return: The description of this ScheduledJob.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ScheduledJob.
        Details describing the Scheduled Job.


        :param description: The description of this ScheduledJob.
        :type: str
        """
        self._description = description

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this ScheduledJob.
        the type of scheduling this Scheduled Job follows

        Allowed values for this property are: "ONETIME", "RECURRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The schedule_type of this ScheduledJob.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this ScheduledJob.
        the type of scheduling this Scheduled Job follows


        :param schedule_type: The schedule_type of this ScheduledJob.
        :type: str
        """
        allowed_values = ["ONETIME", "RECURRING"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            schedule_type = 'UNKNOWN_ENUM_VALUE'
        self._schedule_type = schedule_type

    @property
    def time_next_execution(self):
        """
        Gets the time_next_execution of this ScheduledJob.
        the time of the next execution of this Scheduled Job


        :return: The time_next_execution of this ScheduledJob.
        :rtype: datetime
        """
        return self._time_next_execution

    @time_next_execution.setter
    def time_next_execution(self, time_next_execution):
        """
        Sets the time_next_execution of this ScheduledJob.
        the time of the next execution of this Scheduled Job


        :param time_next_execution: The time_next_execution of this ScheduledJob.
        :type: datetime
        """
        self._time_next_execution = time_next_execution

    @property
    def time_last_execution(self):
        """
        Gets the time_last_execution of this ScheduledJob.
        the time of the last execution of this Scheduled Job


        :return: The time_last_execution of this ScheduledJob.
        :rtype: datetime
        """
        return self._time_last_execution

    @time_last_execution.setter
    def time_last_execution(self, time_last_execution):
        """
        Sets the time_last_execution of this ScheduledJob.
        the time of the last execution of this Scheduled Job


        :param time_last_execution: The time_last_execution of this ScheduledJob.
        :type: datetime
        """
        self._time_last_execution = time_last_execution

    @property
    def interval_type(self):
        """
        Gets the interval_type of this ScheduledJob.
        the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)

        Allowed values for this property are: "HOUR", "DAY", "WEEK", "MONTH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The interval_type of this ScheduledJob.
        :rtype: str
        """
        return self._interval_type

    @interval_type.setter
    def interval_type(self, interval_type):
        """
        Sets the interval_type of this ScheduledJob.
        the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)


        :param interval_type: The interval_type of this ScheduledJob.
        :type: str
        """
        allowed_values = ["HOUR", "DAY", "WEEK", "MONTH"]
        if not value_allowed_none_or_none_sentinel(interval_type, allowed_values):
            interval_type = 'UNKNOWN_ENUM_VALUE'
        self._interval_type = interval_type

    @property
    def interval_value(self):
        """
        Gets the interval_value of this ScheduledJob.
        the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)


        :return: The interval_value of this ScheduledJob.
        :rtype: str
        """
        return self._interval_value

    @interval_value.setter
    def interval_value(self, interval_value):
        """
        Sets the interval_value of this ScheduledJob.
        the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)


        :param interval_value: The interval_value of this ScheduledJob.
        :type: str
        """
        self._interval_value = interval_value

    @property
    def managed_instances(self):
        """
        Gets the managed_instances of this ScheduledJob.
        the list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups)


        :return: The managed_instances of this ScheduledJob.
        :rtype: list[Id]
        """
        return self._managed_instances

    @managed_instances.setter
    def managed_instances(self, managed_instances):
        """
        Sets the managed_instances of this ScheduledJob.
        the list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups)


        :param managed_instances: The managed_instances of this ScheduledJob.
        :type: list[Id]
        """
        self._managed_instances = managed_instances

    @property
    def managed_instance_groups(self):
        """
        Gets the managed_instance_groups of this ScheduledJob.
        the list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances)


        :return: The managed_instance_groups of this ScheduledJob.
        :rtype: list[Id]
        """
        return self._managed_instance_groups

    @managed_instance_groups.setter
    def managed_instance_groups(self, managed_instance_groups):
        """
        Sets the managed_instance_groups of this ScheduledJob.
        the list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances)


        :param managed_instance_groups: The managed_instance_groups of this ScheduledJob.
        :type: list[Id]
        """
        self._managed_instance_groups = managed_instance_groups

    @property
    def operation_type(self):
        """
        Gets the operation_type of this ScheduledJob.
        the type of operation this Scheduled Job performs

        Allowed values for this property are: "INSTALL", "UPDATE", "REMOVE", "UPDATEALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this ScheduledJob.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this ScheduledJob.
        the type of operation this Scheduled Job performs


        :param operation_type: The operation_type of this ScheduledJob.
        :type: str
        """
        allowed_values = ["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def update_type(self):
        """
        Gets the update_type of this ScheduledJob.
        Type of the update (only if operation type is UPDATE_ALL_PACKAGES)

        Allowed values for this property are: "SECURITY", "BUGFIX", "ENHANCEMENT", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The update_type of this ScheduledJob.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this ScheduledJob.
        Type of the update (only if operation type is UPDATE_ALL_PACKAGES)


        :param update_type: The update_type of this ScheduledJob.
        :type: str
        """
        allowed_values = ["SECURITY", "BUGFIX", "ENHANCEMENT", "ALL"]
        if not value_allowed_none_or_none_sentinel(update_type, allowed_values):
            update_type = 'UNKNOWN_ENUM_VALUE'
        self._update_type = update_type

    @property
    def package_names(self):
        """
        Gets the package_names of this ScheduledJob.
        the names of the packages (only if operation type is INSTALL/UPDATE/REMOVE_PACKAGE)


        :return: The package_names of this ScheduledJob.
        :rtype: list[PackageName]
        """
        return self._package_names

    @package_names.setter
    def package_names(self, package_names):
        """
        Sets the package_names of this ScheduledJob.
        the names of the packages (only if operation type is INSTALL/UPDATE/REMOVE_PACKAGE)


        :param package_names: The package_names of this ScheduledJob.
        :type: list[PackageName]
        """
        self._package_names = package_names

    @property
    def work_requests(self):
        """
        Gets the work_requests of this ScheduledJob.
        list of Work Requests associated with this Scheduled Job


        :return: The work_requests of this ScheduledJob.
        :rtype: list[Id]
        """
        return self._work_requests

    @work_requests.setter
    def work_requests(self, work_requests):
        """
        Sets the work_requests of this ScheduledJob.
        list of Work Requests associated with this Scheduled Job


        :param work_requests: The work_requests of this ScheduledJob.
        :type: list[Id]
        """
        self._work_requests = work_requests

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ScheduledJob.
        The current state of the Scheduled Job.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ScheduledJob.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledJob.
        The current state of the Scheduled Job.


        :param lifecycle_state: The lifecycle_state of this ScheduledJob.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduledJob.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ScheduledJob.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduledJob.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ScheduledJob.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduledJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ScheduledJob.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduledJob.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ScheduledJob.
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

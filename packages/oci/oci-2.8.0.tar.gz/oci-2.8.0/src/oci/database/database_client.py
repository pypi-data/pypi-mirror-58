# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel
from .models import database_type_mapping
missing = Sentinel("Missing")


class DatabaseClient(object):
    """
    The API for the Database Service.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default is that the client never times out. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']
        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'timeout': kwargs.get('timeout'),
            'base_path': '/20160918',
            'service_endpoint_template': 'https://database.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("database", config, signer, database_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self._config = config
        self._kwargs = kwargs

    def activate_exadata_infrastructure(self, exadata_infrastructure_id, activate_exadata_infrastructure_details, **kwargs):
        """
        Activate ExadataInfrastructure
        Activates the specified Exadata infrastructure.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ActivateExadataInfrastructureDetails activate_exadata_infrastructure_details: (required)
            The activation details for the Exadata infrastructure.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExadataInfrastructure`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/actions/activate"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "activate_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=activate_exadata_infrastructure_details,
                response_type="ExadataInfrastructure")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=activate_exadata_infrastructure_details,
                response_type="ExadataInfrastructure")

    def change_autonomous_container_database_compartment(self, change_compartment_details, autonomous_container_database_id, **kwargs):
        """
        ChangeAutonomousContainerDatabaseCompartment
        Move the Autonomous Container Database and its dependent resources to the specified compartment.
        For more information about moving Autonomous Container Databases, see
        `Moving Database Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes


        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move Autonomous Container Database to a different compartment

        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousContainerDatabases/{autonomousContainerDatabaseId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_autonomous_container_database_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousContainerDatabaseId": autonomous_container_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)

    def change_autonomous_database_compartment(self, change_compartment_details, autonomous_database_id, **kwargs):
        """
        ChangeAutonomousDatabaseCompartment
        Move the Autonomous Database and its dependent resources to the specified compartment.
        For more information about moving Autonomous Databases, see
        `Moving Database Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes


        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move Autonomous Database to a different compartment

        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_autonomous_database_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)

    def change_autonomous_exadata_infrastructure_compartment(self, change_compartment_details, autonomous_exadata_infrastructure_id, **kwargs):
        """
        ChangeAutonomousExadataInfrastructureCompartment
        Move the Autonomous Exadata Infrastructure and its dependent resources to the specified compartment.
        For more information about moving Autonomous Exadata Infrastructures, see
        `Moving Database Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes


        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move Autonomous Exadata Infrastructure to a different compartment

        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructures/{autonomousExadataInfrastructureId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_autonomous_exadata_infrastructure_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousExadataInfrastructureId": autonomous_exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)

    def change_backup_destination_compartment(self, change_compartment_details, backup_destination_id, **kwargs):
        """
        ChangeBackupDestinationCompartment
        Move the backup destination and its dependent resources to the specified compartment.
        For more information about moving backup destinations, see
        `Moving Database Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes


        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move backup destination to a different compartment

        :param str backup_destination_id: (required)
            The `OCID`__ of the backup destination.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backupDestinations/{backupDestinationId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_backup_destination_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupDestinationId": backup_destination_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)

    def change_db_system_compartment(self, change_compartment_details, db_system_id, **kwargs):
        """
        ChangeDbSystemCompartment
        Move the DB system and its dependent resources to the specified compartment.
        For more information about moving DB systems, see
        `Moving Database Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/databaseoverview.htm#moveRes


        :param ChangeCompartmentDetails change_compartment_details: (required)
            Request to move Db System to a different compartment

        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_db_system_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_compartment_details)

    def change_exadata_infrastructure_compartment(self, change_exadata_infrastructure_compartment_details, exadata_infrastructure_id, **kwargs):
        """
        ChangeExadataInfrastructureCompartment
        To move an Exadata infrastructure and its dependent resources to another compartment, use the
        :func:`change_exadata_infrastructure_compartment` operation.


        :param ChangeExadataInfrastructureCompartmentDetails change_exadata_infrastructure_compartment_details: (required)
            Request to move Exadata infrastructure to a different compartment

        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_exadata_infrastructure_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_exadata_infrastructure_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_exadata_infrastructure_compartment_details)

    def change_vm_cluster_compartment(self, change_vm_cluster_compartment_details, vm_cluster_id, **kwargs):
        """
        ChangeVmClusterCompartment
        To move a VM cluster and its dependent resources to another compartment, use the
        :func:`change_vm_cluster_compartment` operation.


        :param ChangeVmClusterCompartmentDetails change_vm_cluster_compartment_details: (required)
            Request to move VM cluster to a different compartment

        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vmClusters/{vmClusterId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_vm_cluster_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vmClusterId": vm_cluster_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_vm_cluster_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_vm_cluster_compartment_details)

    def complete_external_backup_job(self, backup_id, complete_external_backup_job_details, **kwargs):
        """
        CompleteExternalBackupJob
        Changes the status of the standalone backup resource to `ACTIVE` after the backup is created from the on-premises database and placed in Oracle Cloud Infrastructure Object Storage.

        **Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See `Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud`__ for more information.

        __ https://docs.cloud.oracle.com/Content/Database/Tasks/mig-onprembackup.htm


        :param str backup_id: (required)
            The backup `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param CompleteExternalBackupJobDetails complete_external_backup_job_details: (required)
            Updates the status of the backup resource.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExternalBackupJob`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/externalBackupJobs/{backupId}/actions/complete"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "complete_external_backup_job got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupId": backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=complete_external_backup_job_details,
                response_type="ExternalBackupJob")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=complete_external_backup_job_details,
                response_type="ExternalBackupJob")

    def create_autonomous_container_database(self, create_autonomous_container_database_details, **kwargs):
        """
        CreateAutonomousContainerDatabase
        Create a new Autonomous Container Database in the specified Autonomous Exadata Infrastructure.


        :param CreateAutonomousContainerDatabaseDetails create_autonomous_container_database_details: (required)
            Request to create an Autonomous Container Database in a specified Autonomous Exadata Infrastructure.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousContainerDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousContainerDatabases"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_autonomous_container_database got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_container_database_details,
                response_type="AutonomousContainerDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_container_database_details,
                response_type="AutonomousContainerDatabase")

    def create_autonomous_data_warehouse(self, create_autonomous_data_warehouse_details, **kwargs):
        """
        Creates a new Autonomous Data Warehouse.
        **Deprecated.** To create a new Autonomous Data Warehouse, use the :func:`create_autonomous_database` operation and specify `DW` as the workload type.


        :param CreateAutonomousDataWarehouseDetails create_autonomous_data_warehouse_details: (required)
            Request to create a new Autonomous Data Warehouse.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouse`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_autonomous_data_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_data_warehouse_details,
                response_type="AutonomousDataWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_data_warehouse_details,
                response_type="AutonomousDataWarehouse")

    def create_autonomous_data_warehouse_backup(self, create_autonomous_data_warehouse_backup_details, **kwargs):
        """
        Creates a new Autonomous Data Warehouse backup for the specified database.
        **Deprecated.** To create a new Autonomous Data Warehouse backup for a specified database, use the :func:`create_autonomous_database_backup` operation.


        :param CreateAutonomousDataWarehouseBackupDetails create_autonomous_data_warehouse_backup_details: (required)
            Request to create a new Autonomous Data Warehouse backup.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouseBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouseBackups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_autonomous_data_warehouse_backup got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_data_warehouse_backup_details,
                response_type="AutonomousDataWarehouseBackup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_data_warehouse_backup_details,
                response_type="AutonomousDataWarehouseBackup")

    def create_autonomous_database(self, create_autonomous_database_details, **kwargs):
        """
        Creates a new Autonomous Database.
        Creates a new Autonomous Database.


        :param CreateAutonomousDatabaseBase create_autonomous_database_details: (required)
            Request to create a new Autonomous Database.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_autonomous_database got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_database_details,
                response_type="AutonomousDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_database_details,
                response_type="AutonomousDatabase")

    def create_autonomous_database_backup(self, create_autonomous_database_backup_details, **kwargs):
        """
        Creates a new Autonomous Database backup for the specified database.
        Creates a new Autonomous Database backup for the specified database based on the provided request parameters.


        :param CreateAutonomousDatabaseBackupDetails create_autonomous_database_backup_details: (required)
            Request to create a new Autonomous Database backup.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabaseBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabaseBackups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_autonomous_database_backup got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_database_backup_details,
                response_type="AutonomousDatabaseBackup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_autonomous_database_backup_details,
                response_type="AutonomousDatabaseBackup")

    def create_backup(self, create_backup_details, **kwargs):
        """
        CreateBackup
        Creates a new backup in the specified database based on the request parameters you provide. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.


        :param CreateBackupDetails create_backup_details: (required)
            Request to create a new database backup.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Backup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_backup got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_backup_details,
                response_type="Backup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_backup_details,
                response_type="Backup")

    def create_backup_destination(self, create_backup_destination_details, **kwargs):
        """
        CreateBackupDestination
        Creates a backup destination.


        :param CreateBackupDestinationDetails create_backup_destination_details: (required)
            Request to create a new backup destination.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.BackupDestination`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backupDestinations"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_backup_destination got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_backup_destination_details,
                response_type="BackupDestination")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_backup_destination_details,
                response_type="BackupDestination")

    def create_data_guard_association(self, database_id, create_data_guard_association_details, **kwargs):
        """
        Creates a Data Guard association.
        Creates a new Data Guard association.  A Data Guard association represents the replication relationship between the
        specified database and a peer database. For more information, see `Using Oracle Data Guard`__.

        All Oracle Cloud Infrastructure resources, including Data Guard associations, get an Oracle-assigned, unique ID
        called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response.
        You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the
        resource in the Console. For more information, see
        `Resource Identifiers`__.

        __ https://docs.cloud.oracle.com/Content/Database/Tasks/usingdataguard.htm
        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param CreateDataGuardAssociationDetails create_data_guard_association_details: (required)
            A request to create a Data Guard association.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_data_guard_association_details,
                response_type="DataGuardAssociation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_data_guard_association_details,
                response_type="DataGuardAssociation")

    def create_db_home(self, create_db_home_with_db_system_id_details, **kwargs):
        """
        CreateDbHome
        Creates a new database home in the specified DB system based on the request parameters you provide.


        :param CreateDbHomeBase create_db_home_with_db_system_id_details: (required)
            Request to create a new database home.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbHome`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_db_home got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_db_home_with_db_system_id_details,
                response_type="DbHome")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_db_home_with_db_system_id_details,
                response_type="DbHome")

    def create_exadata_infrastructure(self, create_exadata_infrastructure_details, **kwargs):
        """
        CreateExadataInfrastructure
        Create Exadata infrastructure.


        :param CreateExadataInfrastructureDetails create_exadata_infrastructure_details: (required)
            Request to create Exadata infrastructure.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExadataInfrastructure`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_exadata_infrastructure_details,
                response_type="ExadataInfrastructure")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_exadata_infrastructure_details,
                response_type="ExadataInfrastructure")

    def create_external_backup_job(self, create_external_backup_job_details, **kwargs):
        """
        CreateExternalBackupJob
        Creates a new backup resource and returns the information the caller needs to back up an on-premises Oracle Database to Oracle Cloud Infrastructure.

        **Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See `Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud`__ for more information.

        __ https://docs.cloud.oracle.com/Content/Database/Tasks/mig-onprembackup.htm


        :param CreateExternalBackupJobDetails create_external_backup_job_details: (required)
            Request to create a cloud backup resource for a database running outside the cloud.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExternalBackupJob`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/externalBackupJobs"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_external_backup_job got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_external_backup_job_details,
                response_type="ExternalBackupJob")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_external_backup_job_details,
                response_type="ExternalBackupJob")

    def create_vm_cluster(self, create_vm_cluster_details, **kwargs):
        """
        CreateVmCluster
        Creates a VM cluster.


        :param CreateVmClusterDetails create_vm_cluster_details: (required)
            Request to create a VM cluster.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmCluster`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vmClusters"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_vm_cluster got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_vm_cluster_details,
                response_type="VmCluster")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_vm_cluster_details,
                response_type="VmCluster")

    def create_vm_cluster_network(self, exadata_infrastructure_id, vm_cluster_network_details, **kwargs):
        """
        CreateVmClusterNetwork
        Creates the VM cluster network.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param VmClusterNetworkDetails vm_cluster_network_details: (required)
            Request to create the VM cluster network.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmClusterNetwork`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_vm_cluster_network got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=vm_cluster_network_details,
                response_type="VmClusterNetwork")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=vm_cluster_network_details,
                response_type="VmClusterNetwork")

    def db_node_action(self, db_node_id, action, **kwargs):
        """
        DbNodeAction
        Performs one of the following power actions on the specified DB node:
        - start - power on
        - stop - power off
        - softreset - ACPI shutdown and power on
        - reset - power off and power on

        **Note:** Stopping a node affects billing differently, depending on the type of DB system:
        *Bare metal and Exadata DB systems* - The _stop_ state has no effect on the resources you consume.
        Billing continues for DB nodes that you stop, and related resources continue
        to apply against any relevant quotas. You must terminate the DB system
        (:func:`terminate_db_system`)
        to remove its resources from billing and quotas.
        *Virtual machine DB systems* - Stopping a node stops billing for all OCPUs associated with that node, and billing resumes when you restart the node.


        :param str db_node_id: (required)
            The database node `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str action: (required)
            The action to perform on the DB Node.

            Allowed values are: "STOP", "START", "SOFTRESET", "RESET"

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbNode`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbNodes/{dbNodeId}"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "db_node_action got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbNodeId": db_node_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "action": action
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DbNode")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="DbNode")

    def delete_autonomous_data_warehouse(self, autonomous_data_warehouse_id, **kwargs):
        """
        Deletes the specified Autonomous Data Warehouse.
        **Deprecated.** To delete an Autonomous Data Warehouse, use the :func:`delete_autonomous_database` operation.


        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses/{autonomousDataWarehouseId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_autonomous_data_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseId": autonomous_data_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_autonomous_database(self, autonomous_database_id, **kwargs):
        """
        Deletes the specified Autonomous Database.
        Deletes the specified Autonomous Database.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_autonomous_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_backup(self, backup_id, **kwargs):
        """
        DeleteBackup
        Deletes a full backup. You cannot delete automatic backups using this API.


        :param str backup_id: (required)
            The backup `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups/{backupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupId": backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_backup_destination(self, backup_destination_id, **kwargs):
        """
        DeleteBackupDestination
        Deletes a backup destination.


        :param str backup_destination_id: (required)
            The `OCID`__ of the backup destination.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backupDestinations/{backupDestinationId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_backup_destination got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupDestinationId": backup_destination_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_db_home(self, db_home_id, **kwargs):
        """
        DeleteDbHome
        Deletes a DB Home. The DB Home and its database data are local to the DB system and will be lost when it is deleted. Oracle recommends that you back up any data in the DB system prior to deleting it.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param bool perform_final_backup: (optional)
            Whether to perform a final backup of the database or not. Default is false. If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups to work.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "perform_final_backup"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_db_home got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "performFinalBackup": kwargs.get("perform_final_backup", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def delete_exadata_infrastructure(self, exadata_infrastructure_id, **kwargs):
        """
        Deletes the specified Exadata infrastructure.
        Deletes the Exadata infrastructure.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_vm_cluster(self, vm_cluster_id, **kwargs):
        """
        Deletes the specified VM cluster.
        Deletes the specified VM cluster.


        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vmClusters/{vmClusterId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_vm_cluster got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vmClusterId": vm_cluster_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_vm_cluster_network(self, exadata_infrastructure_id, vm_cluster_network_id, **kwargs):
        """
        Deletes the specified VM cluster network.
        Deletes the specified VM cluster network.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks/{vmClusterNetworkId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_vm_cluster_network got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id,
            "vmClusterNetworkId": vm_cluster_network_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def deregister_autonomous_database_data_safe(self, autonomous_database_id, **kwargs):
        """
        Asynchronously deregisters Data Safe for this Autonomous Database.
        Asynchronously deregisters this Autonomous Database with Data Safe.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/actions/deregisterDataSafe"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "deregister_autonomous_database_data_safe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def download_exadata_infrastructure_config_file(self, exadata_infrastructure_id, **kwargs):
        """
        Downloads the configuration file for the specified Exadata infrastructure.
        Downloads the configuration file for the specified Exadata infrastructure.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/actions/downloadConfigFile"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "download_exadata_infrastructure_config_file got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def download_vm_cluster_network_config_file(self, exadata_infrastructure_id, vm_cluster_network_id, **kwargs):
        """
        Downloads the configuration file for the specified VM Cluster Network.
        Downloads the configuration file for the specified VM Cluster Network.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks/{vmClusterNetworkId}/actions/downloadConfigFile"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "download_vm_cluster_network_config_file got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id,
            "vmClusterNetworkId": vm_cluster_network_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def failover_data_guard_association(self, database_id, data_guard_association_id, failover_data_guard_association_details, **kwargs):
        """
        Performs a failover to transition a standby database into the primary database role.
        Performs a failover to transition the standby database identified by the `databaseId` parameter into the
        specified Data Guard association's primary role after the existing primary database fails or becomes unreachable.

        A failover might result in data loss depending on the protection mode in effect at the time of the primary
        database failure.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param FailoverDataGuardAssociationDetails failover_data_guard_association_details: (required)
            A request to perform a failover, transitioning a standby database into a primary database.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}/actions/failover"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "failover_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=failover_data_guard_association_details,
                response_type="DataGuardAssociation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=failover_data_guard_association_details,
                response_type="DataGuardAssociation")

    def generate_autonomous_data_warehouse_wallet(self, autonomous_data_warehouse_id, generate_autonomous_data_warehouse_wallet_details, **kwargs):
        """
        Creates and downloads a wallet for the specified Autonomous Data Warehouse.
        **Deprecated.** To create and download a wallet for an Autonomous Data Warehouse, use the :func:`generate_autonomous_database_wallet` operation.


        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param GenerateAutonomousDataWarehouseWalletDetails generate_autonomous_data_warehouse_wallet_details: (required)
            Request to create a new Autonomous Data Warehouse wallet.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses/{autonomousDataWarehouseId}/actions/generateWallet"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "generate_autonomous_data_warehouse_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseId": autonomous_data_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=generate_autonomous_data_warehouse_wallet_details,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=generate_autonomous_data_warehouse_wallet_details,
                response_type="stream")

    def generate_autonomous_database_wallet(self, autonomous_database_id, generate_autonomous_database_wallet_details, **kwargs):
        """
        Creates and downloads a wallet for the specified Autonomous Database.
        Creates and downloads a wallet for the specified Autonomous Database.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param GenerateAutonomousDatabaseWalletDetails generate_autonomous_database_wallet_details: (required)
            Request to create a new Autonomous Database wallet.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/actions/generateWallet"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "generate_autonomous_database_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=generate_autonomous_database_wallet_details,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=generate_autonomous_database_wallet_details,
                response_type="stream")

    def generate_recommended_vm_cluster_network(self, exadata_infrastructure_id, generate_recommended_network_details, **kwargs):
        """
        Generates a recommended VM cluster network configuration.
        Generates a recommended VM cluster network configuration.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param GenerateRecommendedNetworkDetails generate_recommended_network_details: (required)
            Request to generate a recommended VM cluster network configuration.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmClusterNetworkDetails`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks/actions/generateRecommendedNetwork"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "generate_recommended_vm_cluster_network got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=generate_recommended_network_details,
                response_type="VmClusterNetworkDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=generate_recommended_network_details,
                response_type="VmClusterNetworkDetails")

    def get_autonomous_container_database(self, autonomous_container_database_id, **kwargs):
        """
        GetAutonomousContainerDatabase
        Gets information about the specified Autonomous Container Database.


        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousContainerDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousContainerDatabases/{autonomousContainerDatabaseId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_container_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousContainerDatabaseId": autonomous_container_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousContainerDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousContainerDatabase")

    def get_autonomous_data_warehouse(self, autonomous_data_warehouse_id, **kwargs):
        """
        Gets the details of the specified Autonomous Data Warehouse.
        **Deprecated.** To get the details of an Autonomous Data Warehouse, use the :func:`get_autonomous_database` operation.


        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouse`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses/{autonomousDataWarehouseId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_data_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseId": autonomous_data_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouse")

    def get_autonomous_data_warehouse_backup(self, autonomous_data_warehouse_backup_id, **kwargs):
        """
        Gets information about the specified Autonomous Data Warehouse backup.
        **Deprecated.** To get information about a specified Autonomous Data Warehouse backup, use the :func:`get_autonomous_database_backup` operation.


        :param str autonomous_data_warehouse_backup_id: (required)
            The `OCID`__ of the Autonomous Data Warehouse backup.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouseBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouseBackups/{autonomousDataWarehouseBackupId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_data_warehouse_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseBackupId": autonomous_data_warehouse_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouseBackup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouseBackup")

    def get_autonomous_database(self, autonomous_database_id, **kwargs):
        """
        Gets the details of the specified Autonomous Database.
        Gets the details of the specified Autonomous Database.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabase")

    def get_autonomous_database_backup(self, autonomous_database_backup_id, **kwargs):
        """
        Gets information about the specified Autonomous Database backup.
        Gets information about the specified Autonomous Database backup.


        :param str autonomous_database_backup_id: (required)
            The `OCID`__ of the Autonomous Database backup.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabaseBackup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabaseBackups/{autonomousDatabaseBackupId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_database_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseBackupId": autonomous_database_backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabaseBackup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabaseBackup")

    def get_autonomous_database_regional_wallet(self, **kwargs):
        """
        Get the regional wallet details for Autonomous Databases.
        Gets the Autonomous Database regional wallet details.


        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabaseWallet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/wallet"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_database_regional_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                response_type="AutonomousDatabaseWallet")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                response_type="AutonomousDatabaseWallet")

    def get_autonomous_database_wallet(self, autonomous_database_id, **kwargs):
        """
        Get the wallet for the specified Autonomous Database.
        Gets the wallet details for the specified Autonomous Database.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabaseWallet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/wallet"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_database_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabaseWallet")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabaseWallet")

    def get_autonomous_exadata_infrastructure(self, autonomous_exadata_infrastructure_id, **kwargs):
        """
        GetAutonomousExadataInfrastructure
        Gets information about the specified Autonomous Exadata Infrastructure.


        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousExadataInfrastructure`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructures/{autonomousExadataInfrastructureId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_autonomous_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousExadataInfrastructureId": autonomous_exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousExadataInfrastructure")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousExadataInfrastructure")

    def get_backup(self, backup_id, **kwargs):
        """
        GetBackup
        Gets information about the specified backup.


        :param str backup_id: (required)
            The backup `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Backup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups/{backupId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backup got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupId": backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Backup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Backup")

    def get_backup_destination(self, backup_destination_id, **kwargs):
        """
        GetBackupDestination
        Gets information about the specified backup destination.


        :param str backup_destination_id: (required)
            The `OCID`__ of the backup destination.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.BackupDestination`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backupDestinations/{backupDestinationId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_backup_destination got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupDestinationId": backup_destination_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BackupDestination")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="BackupDestination")

    def get_data_guard_association(self, database_id, data_guard_association_id, **kwargs):
        """
        Gets configuration information for the specified database and Data Guard association.
        Gets the specified Data Guard association's configuration information.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DataGuardAssociation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DataGuardAssociation")

    def get_database(self, database_id, **kwargs):
        """
        GetDatabase
        Gets information about a specific database.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Database`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Database")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Database")

    def get_db_home(self, db_home_id, **kwargs):
        """
        GetDbHome
        Gets information about the specified database home.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbHome`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_db_home got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DbHome")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DbHome")

    def get_db_home_patch(self, db_home_id, patch_id, **kwargs):
        """
        GetDbHomePatch
        Gets information about a specified patch package.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str patch_id: (required)
            The `OCID`__ of the patch.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Patch`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patches/{patchId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_db_home_patch got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id,
            "patchId": patch_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Patch")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Patch")

    def get_db_home_patch_history_entry(self, db_home_id, patch_history_entry_id, **kwargs):
        """
        GetDbHomePatchHistoryEntry
        Gets the patch history details for the specified patchHistoryEntryId


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str patch_history_entry_id: (required)
            The `OCID`__ of the patch history entry.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.PatchHistoryEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patchHistoryEntries/{patchHistoryEntryId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_db_home_patch_history_entry got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id,
            "patchHistoryEntryId": patch_history_entry_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PatchHistoryEntry")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PatchHistoryEntry")

    def get_db_node(self, db_node_id, **kwargs):
        """
        GetDbNode
        Gets information about the specified database node.


        :param str db_node_id: (required)
            The database node `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbNode`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbNodes/{dbNodeId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_db_node got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbNodeId": db_node_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DbNode")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DbNode")

    def get_db_system(self, db_system_id, **kwargs):
        """
        GetDbSystem
        Gets information about the specified DB system.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbSystem`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_db_system got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DbSystem")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DbSystem")

    def get_db_system_patch(self, db_system_id, patch_id, **kwargs):
        """
        GetDbSystemPatch
        Gets information about a specified patch package.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str patch_id: (required)
            The `OCID`__ of the patch.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Patch`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patches/{patchId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_db_system_patch got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id,
            "patchId": patch_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Patch")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Patch")

    def get_db_system_patch_history_entry(self, db_system_id, patch_history_entry_id, **kwargs):
        """
        GetDbSystemPatchHistoryEntry
        Gets the patch history details for the specified patchHistoryEntryId.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str patch_history_entry_id: (required)
            The `OCID`__ of the patch history entry.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.PatchHistoryEntry`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patchHistoryEntries/{patchHistoryEntryId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_db_system_patch_history_entry got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id,
            "patchHistoryEntryId": patch_history_entry_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PatchHistoryEntry")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PatchHistoryEntry")

    def get_exadata_infrastructure(self, exadata_infrastructure_id, **kwargs):
        """
        GetExadataInfrastructure
        Gets information about the specified Exadata infrastructure.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExadataInfrastructure`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExadataInfrastructure")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExadataInfrastructure")

    def get_exadata_infrastructure_ocpus(self, autonomous_exadata_infrastructure_id, **kwargs):
        """
        Gets details of the available and consumed OCPUs for the specified Autonomous Exadata Infrastructure instance.


        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.OCPUs`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructures/{autonomousExadataInfrastructureId}/ocpus"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_exadata_infrastructure_ocpus got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousExadataInfrastructureId": autonomous_exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OCPUs")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OCPUs")

    def get_exadata_iorm_config(self, db_system_id, **kwargs):
        """
        Gets `IORM` Setting for the requested Exadata DB System.
        The default IORM Settings is pre-created in all the Exadata DB System.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExadataIormConfig`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/ExadataIormConfig"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_exadata_iorm_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExadataIormConfig")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExadataIormConfig")

    def get_external_backup_job(self, backup_id, **kwargs):
        """
        GetExternalBackupJob
        Gets information about the specified external backup job.

        **Note:** This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly. See `Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud`__ for more information.

        __ https://docs.cloud.oracle.com/Content/Database/Tasks/mig-onprembackup.htm


        :param str backup_id: (required)
            The backup `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExternalBackupJob`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/externalBackupJobs/{backupId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_external_backup_job got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupId": backup_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExternalBackupJob")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExternalBackupJob")

    def get_maintenance_run(self, maintenance_run_id, **kwargs):
        """
        GetMaintenanceRun
        Gets information about the specified Maintenance Run.


        :param str maintenance_run_id: (required)
            The Maintenance Run OCID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.MaintenanceRun`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/maintenanceRuns/{maintenanceRunId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_maintenance_run got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "maintenanceRunId": maintenance_run_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="MaintenanceRun")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="MaintenanceRun")

    def get_vm_cluster(self, vm_cluster_id, **kwargs):
        """
        GetVmCluster
        Gets information about the specified VM cluster.


        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmCluster`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vmClusters/{vmClusterId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_vm_cluster got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vmClusterId": vm_cluster_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VmCluster")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VmCluster")

    def get_vm_cluster_network(self, exadata_infrastructure_id, vm_cluster_network_id, **kwargs):
        """
        GetVmClusterNetwork
        Gets information about the specified VM cluster network.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmClusterNetwork`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks/{vmClusterNetworkId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_vm_cluster_network got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id,
            "vmClusterNetworkId": vm_cluster_network_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VmClusterNetwork")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VmClusterNetwork")

    def launch_autonomous_exadata_infrastructure(self, launch_autonomous_exadata_infrastructure_details, **kwargs):
        """
        LaunchAutonomousExadataInfrastructure
        Launches a new Autonomous Exadata Infrastructure in the specified compartment and availability domain.


        :param LaunchAutonomousExadataInfrastructureDetails launch_autonomous_exadata_infrastructure_details: (required)
            Request to launch a Autonomous Exadata Infrastructure.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousExadataInfrastructure`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructures"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "launch_autonomous_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=launch_autonomous_exadata_infrastructure_details,
                response_type="AutonomousExadataInfrastructure")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=launch_autonomous_exadata_infrastructure_details,
                response_type="AutonomousExadataInfrastructure")

    def launch_db_system(self, launch_db_system_details, **kwargs):
        """
        LaunchDbSystem
        Launches a new DB system in the specified compartment and availability domain. The Oracle
        Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

        An initial database is created on the DB system based on the request parameters you provide and some default
        options. For more information,
        see `Default Options for the Initial Database`__.

        __ https://docs.cloud.oracle.com/Content/Database/Tasks/launchingDB.htm#DefaultOptionsfortheInitialDatabase


        :param LaunchDbSystemBase launch_db_system_details: (required)
            Request to launch a DB system.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbSystem`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "launch_db_system got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=launch_db_system_details,
                response_type="DbSystem")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=launch_db_system_details,
                response_type="DbSystem")

    def list_autonomous_container_databases(self, compartment_id, **kwargs):
        """
        ListAutonomousContainerDatabases
        Gets a list of the Autonomous Container Databases in the specified compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_exadata_infrastructure_id: (optional)
            The Autonomous Exadata Infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"

        :param str availability_domain: (optional)
            A filter to return only resources that match the given availability domain exactly.

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousContainerDatabaseSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousContainerDatabases"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "autonomous_exadata_infrastructure_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain",
            "display_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_container_databases got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "BACKUP_IN_PROGRESS", "RESTORING", "RESTORE_FAILED", "RESTARTING", "MAINTENANCE_IN_PROGRESS"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "autonomousExadataInfrastructureId": kwargs.get("autonomous_exadata_infrastructure_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousContainerDatabaseSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousContainerDatabaseSummary]")

    def list_autonomous_data_warehouse_backups(self, **kwargs):
        """
        Gets a list of Autonomous Data Warehouse backups.
        **Deprecated.** To get a list of Autonomous Data Warehouse backups, use the :func:`list_autonomous_database_backups` operation.


        :param str autonomous_data_warehouse_id: (optional)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (optional)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousDataWarehouseBackupSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouseBackups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "autonomous_data_warehouse_id",
            "compartment_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_data_warehouse_backups got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "autonomousDataWarehouseId": kwargs.get("autonomous_data_warehouse_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDataWarehouseBackupSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDataWarehouseBackupSummary]")

    def list_autonomous_data_warehouses(self, compartment_id, **kwargs):
        """
        Gets a list of Autonomous Data Warehouses.
        **Deprecated.** To get a list of Autonomous Data Warehouses, use the :func:`list_autonomous_databases` operation and specify `DW` as the workload type.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousDataWarehouseSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_data_warehouses got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDataWarehouseSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDataWarehouseSummary]")

    def list_autonomous_database_backups(self, **kwargs):
        """
        Gets a list of Autonomous Database backups.
        Gets a list of Autonomous Database backups based on either the `autonomousDatabaseId` or `compartmentId` specified as a query parameter.


        :param str autonomous_database_id: (optional)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (optional)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousDatabaseBackupSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabaseBackups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "autonomous_database_id",
            "compartment_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_database_backups got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "autonomousDatabaseId": kwargs.get("autonomous_database_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDatabaseBackupSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDatabaseBackupSummary]")

    def list_autonomous_databases(self, compartment_id, **kwargs):
        """
        Gets a list of Autonomous Database.
        Gets a list of Autonomous Databases.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str autonomous_container_database_id: (optional)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"

        :param str db_workload: (optional)
            A filter to return only autonomous database resources that match the specified workload type.

            Allowed values are: "OLTP", "DW"

        :param bool is_free_tier: (optional)
            Filter on the value of the resource's 'isFreeTier' property. A value of `true` returns only Always Free resources.
            A value of `false` excludes Always Free resources from the returned results. Omitting this parameter returns both Always Free and paid resources.

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousDatabaseSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "autonomous_container_database_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "db_workload",
            "is_free_tier",
            "display_name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_databases got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'db_workload' in kwargs:
            db_workload_allowed_values = ["OLTP", "DW"]
            if kwargs['db_workload'] not in db_workload_allowed_values:
                raise ValueError(
                    "Invalid value for `db_workload`, must be one of {0}".format(db_workload_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "autonomousContainerDatabaseId": kwargs.get("autonomous_container_database_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "dbWorkload": kwargs.get("db_workload", missing),
            "isFreeTier": kwargs.get("is_free_tier", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDatabaseSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDatabaseSummary]")

    def list_autonomous_db_preview_versions(self, compartment_id, **kwargs):
        """
        Gets a list of supported Autonomous Database versions.
        Gets a list of supported Autonomous Database versions. Note that preview version software is only available for `serverless deployments`__.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for DBWORKLOAD is ascending.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "DBWORKLOAD"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousDbPreviewVersionSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDbPreviewVersions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_request_id",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_db_preview_versions got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["DBWORKLOAD"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDbPreviewVersionSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousDbPreviewVersionSummary]")

    def list_autonomous_exadata_infrastructure_shapes(self, availability_domain, compartment_id, **kwargs):
        """
        ListAutonomousExadataInfrastructureShapes
        Gets a list of the shapes that can be used to launch a new Autonomous Exadata Infrastructure DB system. The shape determines resources to allocate to the DB system (CPU cores, memory and storage).


        :param str availability_domain: (required)
            The name of the Availability Domain.

        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousExadataInfrastructureShapeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructureShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_exadata_infrastructure_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": availability_domain,
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousExadataInfrastructureShapeSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousExadataInfrastructureShapeSummary]")

    def list_autonomous_exadata_infrastructures(self, compartment_id, **kwargs):
        """
        ListAutonomousExadataInfrastructures
        Gets a list of the Autonomous Exadata Infrastructures in the specified compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

              **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"

        :param str availability_domain: (optional)
            A filter to return only resources that match the given availability domain exactly.

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.AutonomousExadataInfrastructureSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructures"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain",
            "display_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_autonomous_exadata_infrastructures got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousExadataInfrastructureSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AutonomousExadataInfrastructureSummary]")

    def list_backup_destination(self, compartment_id, **kwargs):
        """
        ListBackupDestination
        Gets a list of backup destinations in the specified compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str type: (optional)
            A filter to return only resources that match the given type of the Backup Destination.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.BackupDestinationSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backupDestinations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_request_id",
            "type"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_backup_destination got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "type": kwargs.get("type", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BackupDestinationSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BackupDestinationSummary]")

    def list_backups(self, **kwargs):
        """
        ListBackups
        Gets a list of backups based on the databaseId or compartmentId specified. Either one of the query parameters must be provided.


        :param str database_id: (optional)
            The `OCID`__ of the database.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (optional)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.BackupSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "database_id",
            "compartment_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_backups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "databaseId": kwargs.get("database_id", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BackupSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[BackupSummary]")

    def list_data_guard_associations(self, database_id, **kwargs):
        """
        Lists all Data Guard associations for the specified database.
        Lists all Data Guard associations for the specified database.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DataGuardAssociationSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_data_guard_associations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DataGuardAssociationSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DataGuardAssociationSummary]")

    def list_databases(self, compartment_id, db_home_id, **kwargs):
        """
        ListDatabases
        Gets a list of the databases in the specified database home.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str db_home_id: (required)
            A database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DBNAME is ascending. The DBNAME sort order is case sensitive.

            Allowed values are: "DBNAME", "TIMECREATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"

        :param str db_name: (optional)
            A filter to return only resources that match the entire database name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DatabaseSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "db_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_databases got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["DBNAME", "TIMECREATED"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "dbHomeId": db_home_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "dbName": kwargs.get("db_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DatabaseSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DatabaseSummary]")

    def list_db_home_patch_history_entries(self, db_home_id, **kwargs):
        """
        ListDbHomePatchHistoryEntries
        Gets history of the actions taken for patches for the specified database home.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchHistoryEntrySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patchHistoryEntries"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_home_patch_history_entries got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchHistoryEntrySummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchHistoryEntrySummary]")

    def list_db_home_patches(self, db_home_id, **kwargs):
        """
        ListDbHomePatches
        Lists patches applicable to the requested database home.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}/patches"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_home_patches got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchSummary]")

    def list_db_homes(self, compartment_id, **kwargs):
        """
        ListDbHomes
        Gets a list of database homes in the specified DB system and compartment. A database home is a directory where Oracle Database software is installed.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str db_system_id: (optional)
            The DB system `OCID`__. If provided, filters the results to the set of database versions which are supported for the DB system.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_id: (optional)
            The `OCID`__ of the VM cluster.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbHomeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "db_system_id",
            "vm_cluster_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_homes got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "dbSystemId": kwargs.get("db_system_id", missing),
            "vmClusterId": kwargs.get("vm_cluster_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbHomeSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbHomeSummary]")

    def list_db_nodes(self, compartment_id, **kwargs):
        """
        ListDbNodes
        Gets a list of database nodes in the specified DB system and compartment. A database node is a server running database software.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str db_system_id: (optional)
            The DB system `OCID`__. If provided, filters the results to the set of database versions which are supported for the DB system.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_id: (optional)
            The `OCID`__ of the VM cluster.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            Sort by TIMECREATED.  Default order for TIMECREATED is descending.

            Allowed values are: "TIMECREATED"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbNodeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbNodes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "db_system_id",
            "vm_cluster_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_nodes got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "dbSystemId": kwargs.get("db_system_id", missing),
            "vmClusterId": kwargs.get("vm_cluster_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbNodeSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbNodeSummary]")

    def list_db_system_patch_history_entries(self, db_system_id, **kwargs):
        """
        ListDbSystemPatchHistoryEntries
        Gets the history of the patch actions performed on the specified DB system.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchHistoryEntrySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patchHistoryEntries"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_system_patch_history_entries got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchHistoryEntrySummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchHistoryEntrySummary]")

    def list_db_system_patches(self, db_system_id, **kwargs):
        """
        ListDbSystemPatches
        Lists the patches applicable to the requested DB system.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.PatchSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/patches"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_system_patches got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[PatchSummary]")

    def list_db_system_shapes(self, compartment_id, **kwargs):
        """
        ListDbSystemShapes
        Gets a list of the shapes that can be used to launch a new DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str availability_domain: (optional)
            The name of the Availability Domain.

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbSystemShapeSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystemShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "availability_domain",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_system_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbSystemShapeSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbSystemShapeSummary]")

    def list_db_systems(self, compartment_id, **kwargs):
        """
        ListDbSystems
        Gets a list of the DB systems in the specified compartment. You can specify a backupId to list only the DB systems that support creating a database using this backup in this compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str backup_id: (optional)
            The `OCID`__ of the backup. Specify a backupId to list only the DB systems or DB homes that support creating a database using this backup in this compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"

        :param str availability_domain: (optional)
            A filter to return only resources that match the given availability domain exactly.

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbSystemSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "backup_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain",
            "display_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_systems got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "backupId": kwargs.get("backup_id", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "availabilityDomain": kwargs.get("availability_domain", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbSystemSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbSystemSummary]")

    def list_db_versions(self, compartment_id, **kwargs):
        """
        ListDbVersions
        Gets a list of supported Oracle Database versions.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str db_system_shape: (optional)
            If provided, filters the results to the set of database versions which are supported for the given shape.

        :param str db_system_id: (optional)
            The DB system `OCID`__. If provided, filters the results to the set of database versions which are supported for the DB system.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.DbVersionSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbVersions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "db_system_shape",
            "db_system_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_db_versions got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "dbSystemShape": kwargs.get("db_system_shape", missing),
            "dbSystemId": kwargs.get("db_system_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbVersionSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DbVersionSummary]")

    def list_exadata_infrastructures(self, compartment_id, **kwargs):
        """
        ListExadataInfrastructures
        Gets a list of the Exadata infrastructure in the specified compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.ExadataInfrastructureSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "opc_request_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_exadata_infrastructures got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "REQUIRES_ACTIVATION", "ACTIVATING", "ACTIVE", "ACTIVATION_FAILED", "FAILED", "UPDATING", "DELETING", "DELETED", "OFFLINE"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ExadataInfrastructureSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ExadataInfrastructureSummary]")

    def list_gi_versions(self, compartment_id, **kwargs):
        """
        ListGiVersions
        Gets a list of supported GI versions for VM Cluster.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str shape: (optional)
            If provided, filters the results for the given shape.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.GiVersionSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/giVersions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "sort_order",
            "shape"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_gi_versions got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "shape": kwargs.get("shape", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[GiVersionSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[GiVersionSummary]")

    def list_maintenance_runs(self, compartment_id, **kwargs):
        """
        ListMaintenanceRuns
        Gets a list of the Maintenance Runs in the specified compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str target_resource_id: (optional)
            The target resource ID.

        :param str target_resource_type: (optional)
            The type of the target resource.

            Allowed values are: "AUTONOMOUS_EXADATA_INFRASTRUCTURE", "AUTONOMOUS_CONTAINER_DATABASE", "EXADATA_DB_SYSTEM"

        :param str maintenance_type: (optional)
            The maintenance type.

            Allowed values are: "PLANNED", "UNPLANNED"

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIME_SCHEDULED and TIME_ENDED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            **Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted.

            Allowed values are: "TIME_SCHEDULED", "TIME_ENDED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "SCHEDULED", "IN_PROGRESS", "SUCCEEDED", "SKIPPED", "FAILED", "UPDATING"

        :param str availability_domain: (optional)
            A filter to return only resources that match the given availability domain exactly.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.MaintenanceRunSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/maintenanceRuns"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "target_resource_id",
            "target_resource_type",
            "maintenance_type",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_maintenance_runs got unknown kwargs: {!r}".format(extra_kwargs))

        if 'target_resource_type' in kwargs:
            target_resource_type_allowed_values = ["AUTONOMOUS_EXADATA_INFRASTRUCTURE", "AUTONOMOUS_CONTAINER_DATABASE", "EXADATA_DB_SYSTEM"]
            if kwargs['target_resource_type'] not in target_resource_type_allowed_values:
                raise ValueError(
                    "Invalid value for `target_resource_type`, must be one of {0}".format(target_resource_type_allowed_values)
                )

        if 'maintenance_type' in kwargs:
            maintenance_type_allowed_values = ["PLANNED", "UNPLANNED"]
            if kwargs['maintenance_type'] not in maintenance_type_allowed_values:
                raise ValueError(
                    "Invalid value for `maintenance_type`, must be one of {0}".format(maintenance_type_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIME_SCHEDULED", "TIME_ENDED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["SCHEDULED", "IN_PROGRESS", "SUCCEEDED", "SKIPPED", "FAILED", "UPDATING"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "targetResourceId": kwargs.get("target_resource_id", missing),
            "targetResourceType": kwargs.get("target_resource_type", missing),
            "maintenanceType": kwargs.get("maintenance_type", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "availabilityDomain": kwargs.get("availability_domain", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MaintenanceRunSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[MaintenanceRunSummary]")

    def list_vm_cluster_networks(self, exadata_infrastructure_id, compartment_id, **kwargs):
        """
        ListVmClusterNetworks
        Gets a list of the VM cluster networks in the specified compartment.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.VmClusterNetworkSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vm_cluster_networks got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VmClusterNetworkSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VmClusterNetworkSummary]")

    def list_vm_clusters(self, compartment_id, **kwargs):
        """
        ListVmClusters
        Gets a list of the VM clusters in the specified compartment.


        :param str compartment_id: (required)
            The compartment `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str exadata_infrastructure_id: (optional)
            If provided, filters the results for the given Exadata Infrastructure.

        :param int limit: (optional)
            The maximum number of items to return per page.

        :param str page: (optional)
            The pagination token to continue listing from.

        :param str sort_by: (optional)
            The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

            Allowed values are: "TIMECREATED", "DISPLAYNAME"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            A filter to return only resources that match the given lifecycle state exactly.

            Allowed values are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name given. The match is not case sensitive.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.database.models.VmClusterSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vmClusters"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "exadata_infrastructure_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "display_name",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vm_clusters got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "DISPLAYNAME"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "exadataInfrastructureId": kwargs.get("exadata_infrastructure_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "displayName": kwargs.get("display_name", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VmClusterSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[VmClusterSummary]")

    def register_autonomous_database_data_safe(self, autonomous_database_id, **kwargs):
        """
        Asynchronously registers this Autonomous Database with Data Safe.
        Asynchronously registers this Autonomous Database with Data Safe.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/actions/registerDataSafe"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "register_autonomous_database_data_safe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def reinstate_data_guard_association(self, database_id, data_guard_association_id, reinstate_data_guard_association_details, **kwargs):
        """
        Reinstates a database to a Data Guard association standby role.
        Reinstates the database identified by the `databaseId` parameter into the standby role in a Data Guard association.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ReinstateDataGuardAssociationDetails reinstate_data_guard_association_details: (required)
            A request to reinstate a database in a standby role.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}/actions/reinstate"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "reinstate_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=reinstate_data_guard_association_details,
                response_type="DataGuardAssociation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=reinstate_data_guard_association_details,
                response_type="DataGuardAssociation")

    def restart_autonomous_container_database(self, autonomous_container_database_id, **kwargs):
        """
        Rolling restarts the specified Autonomous Container Database.
        Rolling restarts the specified Autonomous Container Database.


        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousContainerDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousContainerDatabases/{autonomousContainerDatabaseId}/actions/restart"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restart_autonomous_container_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousContainerDatabaseId": autonomous_container_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousContainerDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousContainerDatabase")

    def restore_autonomous_data_warehouse(self, autonomous_data_warehouse_id, restore_autonomous_data_warehouse_details, **kwargs):
        """
        Restores an Autonomous Data Warehouse based on the provided request parameters.
        **Deprecated.** To restore an Autonomous Data Warehouse, use the :func:`restore_autonomous_database` operation.


        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreAutonomousDataWarehouseDetails restore_autonomous_data_warehouse_details: (required)
            Request to perform an Autonomous Data Warehouse restore.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouse`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses/{autonomousDataWarehouseId}/actions/restore"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_autonomous_data_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseId": autonomous_data_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_autonomous_data_warehouse_details,
                response_type="AutonomousDataWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_autonomous_data_warehouse_details,
                response_type="AutonomousDataWarehouse")

    def restore_autonomous_database(self, autonomous_database_id, restore_autonomous_database_details, **kwargs):
        """
        Restores an Autonomous Database based on the provided request parameters.
        Restores an Autonomous Database based on the provided request parameters.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreAutonomousDatabaseDetails restore_autonomous_database_details: (required)
            Request to perform an Autonomous Database restore.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/actions/restore"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_autonomous_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_autonomous_database_details,
                response_type="AutonomousDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_autonomous_database_details,
                response_type="AutonomousDatabase")

    def restore_database(self, database_id, restore_database_details, **kwargs):
        """
        RestoreDatabase
        Restore a Database based on the request parameters you provide.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param RestoreDatabaseDetails restore_database_details: (required)
            Request to perform database restore.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Database`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/actions/restore"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "restore_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_database_details,
                response_type="Database")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=restore_database_details,
                response_type="Database")

    def start_autonomous_data_warehouse(self, autonomous_data_warehouse_id, **kwargs):
        """
        Starts the specified autonomous Data Warehouse.
        **Deprecated.** To start an Autonomous Data Warehouse, use the :func:`start_autonomous_database` operation.


        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouse`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses/{autonomousDataWarehouseId}/actions/start"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "start_autonomous_data_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseId": autonomous_data_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouse")

    def start_autonomous_database(self, autonomous_database_id, **kwargs):
        """
        Starts the specified Autonomous Database.
        Starts the specified Autonomous Database.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/actions/start"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "start_autonomous_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabase")

    def stop_autonomous_data_warehouse(self, autonomous_data_warehouse_id, **kwargs):
        """
        Stops the specified Autonomous Data Warehouse.
        **Deprecated.** To stop an Autonomous Data Warehouse, use the :func:`stop_autonomous_database` operation.


        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouse`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses/{autonomousDataWarehouseId}/actions/stop"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "stop_autonomous_data_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseId": autonomous_data_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDataWarehouse")

    def stop_autonomous_database(self, autonomous_database_id, **kwargs):
        """
        Stops the specified Autonomous Database.
        Stops the specified Autonomous Database.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/actions/stop"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "stop_autonomous_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AutonomousDatabase")

    def switchover_data_guard_association(self, database_id, data_guard_association_id, switchover_data_guard_association_details, **kwargs):
        """
        Performs a switchover to transition the primary database of a Data Guard association into a standby role.
        Performs a switchover to transition the primary database of a Data Guard association into a standby role. The
        standby database associated with the `dataGuardAssociationId` assumes the primary database role.

        A switchover guarantees no data loss.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str data_guard_association_id: (required)
            The Data Guard association's `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param SwitchoverDataGuardAssociationDetails switchover_data_guard_association_details: (required)
            Request to swtichover a primary to a standby.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DataGuardAssociation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}/dataGuardAssociations/{dataGuardAssociationId}/actions/switchover"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "switchover_data_guard_association got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id,
            "dataGuardAssociationId": data_guard_association_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=switchover_data_guard_association_details,
                response_type="DataGuardAssociation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=switchover_data_guard_association_details,
                response_type="DataGuardAssociation")

    def terminate_autonomous_container_database(self, autonomous_container_database_id, **kwargs):
        """
        TerminiateAutonomousContainerDatabase
        Terminates an Autonomous Container Database, which permanently deletes the container database and any databases within the container database. The database data is local to the Autonomous Exadata Infrastructure and will be lost when the container database is terminated. Oracle recommends that you back up any data in the Autonomous Container Database prior to terminating it.


        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousContainerDatabases/{autonomousContainerDatabaseId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "terminate_autonomous_container_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousContainerDatabaseId": autonomous_container_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def terminate_autonomous_exadata_infrastructure(self, autonomous_exadata_infrastructure_id, **kwargs):
        """
        TerminateAutonomousExadataInfrastructure
        Terminates an Autonomous Exadata Infrastructure, which permanently deletes the Exadata Infrastructure and any container databases and databases contained in the Exadata Infrastructure. The database data is local to the Autonomous Exadata Infrastructure and will be lost when the system is terminated. Oracle recommends that you back up any data in the Autonomous Exadata Infrastructure prior to terminating it.


        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructures/{autonomousExadataInfrastructureId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "terminate_autonomous_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousExadataInfrastructureId": autonomous_exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def terminate_db_system(self, db_system_id, **kwargs):
        """
        TerminateDbSystem
        Terminates a DB system and permanently deletes it and any databases running on it, and any storage volumes attached to it. The database data is local to the DB system and will be lost when the system is terminated. Oracle recommends that you back up any data in the DB system prior to terminating it.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "terminate_db_system got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def update_autonomous_container_database(self, autonomous_container_database_id, update_autonomous_container_database_details, **kwargs):
        """
        UpdateAutonomousContainerDatabase
        Updates the properties of an Autonomous Container Database, such as the OCPU core count and storage size.


        :param str autonomous_container_database_id: (required)
            The Autonomous Container Database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousContainerDatabaseDetails update_autonomous_container_database_details: (required)
            Request to update the properties of an Autonomous Container Database.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousContainerDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousContainerDatabases/{autonomousContainerDatabaseId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_autonomous_container_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousContainerDatabaseId": autonomous_container_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_container_database_details,
                response_type="AutonomousContainerDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_container_database_details,
                response_type="AutonomousContainerDatabase")

    def update_autonomous_data_warehouse(self, autonomous_data_warehouse_id, update_autonomous_data_warehouse_details, **kwargs):
        """
        Updates the specified Autonomous Data Warehouse with new CPU core count and size.
        **Deprecated.** To update the CPU core count and storage size of an Autonomous Data Warehouse, use the :func:`update_autonomous_database` operation.


        :param str autonomous_data_warehouse_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousDataWarehouseDetails update_autonomous_data_warehouse_details: (required)
            Request to update the properties of an Autonomous Data Warehouse.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDataWarehouse`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDataWarehouses/{autonomousDataWarehouseId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_autonomous_data_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDataWarehouseId": autonomous_data_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_data_warehouse_details,
                response_type="AutonomousDataWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_data_warehouse_details,
                response_type="AutonomousDataWarehouse")

    def update_autonomous_database(self, autonomous_database_id, update_autonomous_database_details, **kwargs):
        """
        Updates the specified Autonomous Database with new OCPU core count and size.
        Updates one or more attributes of the specified Autonomous Database. See the UpdateAutonomousDatabaseDetails resource for a full list of attributes that can be updated.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousDatabaseDetails update_autonomous_database_details: (required)
            Request to update the properties of an Autonomous Database.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousDatabase`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_autonomous_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_database_details,
                response_type="AutonomousDatabase")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_database_details,
                response_type="AutonomousDatabase")

    def update_autonomous_database_regional_wallet(self, update_autonomous_database_wallet_details, **kwargs):
        """
        Update the regional wallet for Autonomous Database.
        Updates the Autonomous Database regional wallet.


        :param UpdateAutonomousDatabaseWalletDetails update_autonomous_database_wallet_details: (required)
            Request to update the properties of Autonomous Database regional wallet.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/wallet"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_autonomous_database_regional_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=update_autonomous_database_wallet_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=update_autonomous_database_wallet_details)

    def update_autonomous_database_wallet(self, autonomous_database_id, update_autonomous_database_wallet_details, **kwargs):
        """
        Updates the wallet for the specified Autonomous Database.
        Updates the wallet for the specified Autonomous Database.


        :param str autonomous_database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousDatabaseWalletDetails update_autonomous_database_wallet_details: (required)
            Request to update the properties of an Autonomous Database wallet.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousDatabases/{autonomousDatabaseId}/wallet"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_autonomous_database_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousDatabaseId": autonomous_database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_database_wallet_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_database_wallet_details)

    def update_autonomous_exadata_infrastructure(self, autonomous_exadata_infrastructure_id, update_autonomous_exadata_infrastructures_details, **kwargs):
        """
        UpdateAutonomousExadataInfrastructure
        Updates the properties of an Autonomous Exadata Infrastructure, such as the CPU core count.


        :param str autonomous_exadata_infrastructure_id: (required)
            The Autonomous Exadata Infrastructure  `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateAutonomousExadataInfrastructureDetails update_autonomous_exadata_infrastructures_details: (required)
            Request to update the properties of a Autonomous Exadata Infrastructure.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.AutonomousExadataInfrastructure`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/autonomousExadataInfrastructures/{autonomousExadataInfrastructureId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_autonomous_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "autonomousExadataInfrastructureId": autonomous_exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_exadata_infrastructures_details,
                response_type="AutonomousExadataInfrastructure")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_autonomous_exadata_infrastructures_details,
                response_type="AutonomousExadataInfrastructure")

    def update_backup_destination(self, backup_destination_id, update_backup_destination_details, **kwargs):
        """
        Updates the specified backup destination.
        If no database is associated with the backup destination:
        - For a RECOVERY_APPLIANCE backup destination, updates the connection string and/or the list of VPC users.
        - For an NFS backup destination, updates the NFS location.


        :param str backup_destination_id: (required)
            The `OCID`__ of the backup destination.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateBackupDestinationDetails update_backup_destination_details: (required)
            For a RECOVERY_APPLIANCE backup destination, request to update the connection string and/or the list of VPC users.
            For an NFS backup destination, request to update the NFS location.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.BackupDestination`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/backupDestinations/{backupDestinationId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_backup_destination got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "backupDestinationId": backup_destination_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_backup_destination_details,
                response_type="BackupDestination")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_backup_destination_details,
                response_type="BackupDestination")

    def update_database(self, database_id, update_database_details, **kwargs):
        """
        UpdateDatabase
        Update a Database based on the request parameters you provide.


        :param str database_id: (required)
            The database `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDatabaseDetails update_database_details: (required)
            Request to perform database update.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.Database`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/databases/{databaseId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_database got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseId": database_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_database_details,
                response_type="Database")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_database_details,
                response_type="Database")

    def update_db_home(self, db_home_id, update_db_home_details, **kwargs):
        """
        UpdateDbHome
        Patches the specified dbHome.


        :param str db_home_id: (required)
            The database home `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbHomeDetails update_db_home_details: (required)
            Request to update the properties of a DB Home.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbHome`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbHomes/{dbHomeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_db_home got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbHomeId": db_home_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_db_home_details,
                response_type="DbHome")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_db_home_details,
                response_type="DbHome")

    def update_db_system(self, db_system_id, update_db_system_details, **kwargs):
        """
        UpdateDbSystem
        Updates the properties of a DB system, such as the CPU core count.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateDbSystemDetails update_db_system_details: (required)
            Request to update the properties of a DB system.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.DbSystem`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_db_system got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_db_system_details,
                response_type="DbSystem")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_db_system_details,
                response_type="DbSystem")

    def update_exadata_infrastructure(self, exadata_infrastructure_id, update_exadata_infrastructure_details, **kwargs):
        """
        Updates the specified Exadata Infrastructure
        Updates the Exadata infrastructure.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateExadataInfrastructureDetails update_exadata_infrastructure_details: (required)
            Request to update the properties of an Exadata infrastructure

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExadataInfrastructure`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_exadata_infrastructure got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_exadata_infrastructure_details,
                response_type="ExadataInfrastructure")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_exadata_infrastructure_details,
                response_type="ExadataInfrastructure")

    def update_exadata_iorm_config(self, db_system_id, exadata_iorm_config_update_details, **kwargs):
        """
        Update `IORM` Settings for the requested Exadata DB System.


        :param str db_system_id: (required)
            The DB system `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param ExadataIormConfigUpdateDetails exadata_iorm_config_update_details: (required)
            Request to perform database update.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.ExadataIormConfig`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dbSystems/{dbSystemId}/ExadataIormConfig"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_exadata_iorm_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dbSystemId": db_system_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=exadata_iorm_config_update_details,
                response_type="ExadataIormConfig")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=exadata_iorm_config_update_details,
                response_type="ExadataIormConfig")

    def update_maintenance_run(self, maintenance_run_id, update_maintenance_run_details, **kwargs):
        """
        UpdateMaintenanceRun
        Updates the properties of a Maintenance Run, such as the state of a Maintenance Run.


        :param str maintenance_run_id: (required)
            The Maintenance Run OCID.

        :param UpdateMaintenanceRunDetails update_maintenance_run_details: (required)
            Request to update the properties of a Maintenance Run.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.MaintenanceRun`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/maintenanceRuns/{maintenanceRunId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_maintenance_run got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "maintenanceRunId": maintenance_run_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_maintenance_run_details,
                response_type="MaintenanceRun")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_maintenance_run_details,
                response_type="MaintenanceRun")

    def update_vm_cluster(self, vm_cluster_id, update_vm_cluster_details, **kwargs):
        """
        Updates the specified VM cluster.
        Updates the specified VM cluster.


        :param str vm_cluster_id: (required)
            The VM cluster `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVmClusterDetails update_vm_cluster_details: (required)
            Request to update the attributes of a VM cluster.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmCluster`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/vmClusters/{vmClusterId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_vm_cluster got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vmClusterId": vm_cluster_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vm_cluster_details,
                response_type="VmCluster")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vm_cluster_details,
                response_type="VmCluster")

    def update_vm_cluster_network(self, exadata_infrastructure_id, vm_cluster_network_id, update_vm_cluster_network_details, **kwargs):
        """
        Updates the specified VM cluster network.
        Updates the specified VM cluster network.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param UpdateVmClusterNetworkDetails update_vm_cluster_network_details: (required)
            Request to update the properties of a VM cluster network.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmClusterNetwork`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks/{vmClusterNetworkId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_vm_cluster_network got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id,
            "vmClusterNetworkId": vm_cluster_network_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vm_cluster_network_details,
                response_type="VmClusterNetwork")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_vm_cluster_network_details,
                response_type="VmClusterNetwork")

    def validate_vm_cluster_network(self, exadata_infrastructure_id, vm_cluster_network_id, **kwargs):
        """
        Validates the specified VM cluster network.
        Validates the specified VM cluster network.


        :param str exadata_infrastructure_id: (required)
            The Exadata infrastructure `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str vm_cluster_network_id: (required)
            The VM cluster network `OCID`__.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique identifier for the request.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (for example, if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.database.models.VmClusterNetwork`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/exadataInfrastructures/{exadataInfrastructureId}/vmClusterNetworks/{vmClusterNetworkId}/actions/validate"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "validate_vm_cluster_network got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInfrastructureId": exadata_infrastructure_id,
            "vmClusterNetworkId": vm_cluster_network_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VmClusterNetwork")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="VmClusterNetwork")

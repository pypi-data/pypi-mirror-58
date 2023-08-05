# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RedirectUri(object):
    """
    An object that defines the redirect URI applied to the original request. The object property values compose the
    redirect URI.

    **NOTE:** The Load Balancing service cannot automatically detect or avoid infinite redirects. Be sure to provide
    meaningful, complete, and correct field values. If any component field of this object has no value, the system
    retains the value from the incoming HTTP request URI.

    For example, if you specify only the protocol field `https`, and the incoming request URI is
    `http://example.com:8080`, the resulting runtime redirect URI is `https://example.com:8080`. The system retains
    the host and port from the incoming URI and does not automatically change the port setting from `8080` to `443`.

    Be sure to configure valid percent-encoding (URL encoding) when needed.

    In addition to static string values, you can use the following tokens to construct the redirect URI. These tokens
    extract values from the incoming HTTP request URI.

    *  {protocol} : The protocol from the incoming HTTP request URI.
    *  {host}     : The domain name from the incoming HTTP request URI.
    *  {port}     : The port from the incoming HTTP request URI.
    *  {path}     : The path from the incoming HTTP request URI.
    *  {query}    : The query string from the incoming HTTP request URI.

    The tokens are case sensitive. For example, `{host}` is a valid token, but `{HOST}` is not.

    You can retain the literal characters of a token when you specify values for the path and query properties of the
    redirect URI. Use a backslash (\\\\) as the escape character for the \\\\, {, and } characters. For example, if the
    incoming HTTP request URI is `/video`, the path property value:

    `/example{path}123\\{path\\}`

    appears in the constructed redirect URI as:

    `/example/video123{path}`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RedirectUri object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this RedirectUri.
        :type protocol: str

        :param host:
            The value to assign to the host property of this RedirectUri.
        :type host: str

        :param port:
            The value to assign to the port property of this RedirectUri.
        :type port: int

        :param path:
            The value to assign to the path property of this RedirectUri.
        :type path: str

        :param query:
            The value to assign to the query property of this RedirectUri.
        :type query: str

        """
        self.swagger_types = {
            'protocol': 'str',
            'host': 'str',
            'port': 'int',
            'path': 'str',
            'query': 'str'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'host': 'host',
            'port': 'port',
            'path': 'path',
            'query': 'query'
        }

        self._protocol = None
        self._host = None
        self._port = None
        self._path = None
        self._query = None

    @property
    def protocol(self):
        """
        Gets the protocol of this RedirectUri.
        The HTTP protocol to use in the redirect URI.

        When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the
        incoming HTTP request URI. Allowed values are:

        *  HTTP
        *  HTTPS
        *  {protocol}

        `{protocol}` is the only valid token for this property. It can appear only once in the value string.

        Example: `HTTPS`


        :return: The protocol of this RedirectUri.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this RedirectUri.
        The HTTP protocol to use in the redirect URI.

        When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the
        incoming HTTP request URI. Allowed values are:

        *  HTTP
        *  HTTPS
        *  {protocol}

        `{protocol}` is the only valid token for this property. It can appear only once in the value string.

        Example: `HTTPS`


        :param protocol: The protocol of this RedirectUri.
        :type: str
        """
        self._protocol = protocol

    @property
    def host(self):
        """
        Gets the host of this RedirectUri.
        The valid domain name (hostname) or IP address to use in the redirect URI.

        When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the
        incoming HTTP request URI.

        All RedirectUri tokens are valid for this property. You can use any token more than once.

        Curly braces are valid in this property only to surround tokens, such as `{host}`

        Examples:

        *  **example.com** appears as `example.com` in the redirect URI.

        *  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the
           incoming HTTP request URI.

        *  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and
           the port is `8081` in the incoming HTTP request URI.


        :return: The host of this RedirectUri.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this RedirectUri.
        The valid domain name (hostname) or IP address to use in the redirect URI.

        When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the
        incoming HTTP request URI.

        All RedirectUri tokens are valid for this property. You can use any token more than once.

        Curly braces are valid in this property only to surround tokens, such as `{host}`

        Examples:

        *  **example.com** appears as `example.com` in the redirect URI.

        *  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the
           incoming HTTP request URI.

        *  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and
           the port is `8081` in the incoming HTTP request URI.


        :param host: The host of this RedirectUri.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this RedirectUri.
        The communication port to use in the redirect URI.

        Valid values include integers from 1 to 65535.

        When this value is null, the service preserves the original port from the incoming HTTP request URI.

        Example: `8081`


        :return: The port of this RedirectUri.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this RedirectUri.
        The communication port to use in the redirect URI.

        Valid values include integers from 1 to 65535.

        When this value is null, the service preserves the original port from the incoming HTTP request URI.

        Example: `8081`


        :param port: The port of this RedirectUri.
        :type: int
        """
        self._port = port

    @property
    def path(self):
        """
        Gets the path of this RedirectUri.
        The HTTP URI path to use in the redirect URI.

        When this value is null, not set, or set to `{path}`, the service preserves the original path from the
        incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, \"\".

        All RedirectUri tokens are valid for this property. You can use any token more than once.

        The path string must begin with `/` if it does not begin with the `{path}` token.

        Examples:

        *  __/example/video/123__ appears as `/example/video/123` in the redirect URI.

        *  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the
           incoming HTTP request URI.

        *  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the
           incoming HTTP request URI.

        *  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video is the path in the
           incoming HTTP request URI.

        *  __/{host}/123__ appears as `/example.com/video/123` in the redirect URI if `example.com` is the hostname
           in the incoming HTTP request URI.

        *  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and
           `123` is the port in the incoming HTTP request URI.

        *  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP
           request URI.


        :return: The path of this RedirectUri.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this RedirectUri.
        The HTTP URI path to use in the redirect URI.

        When this value is null, not set, or set to `{path}`, the service preserves the original path from the
        incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, \"\".

        All RedirectUri tokens are valid for this property. You can use any token more than once.

        The path string must begin with `/` if it does not begin with the `{path}` token.

        Examples:

        *  __/example/video/123__ appears as `/example/video/123` in the redirect URI.

        *  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the
           incoming HTTP request URI.

        *  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the
           incoming HTTP request URI.

        *  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video is the path in the
           incoming HTTP request URI.

        *  __/{host}/123__ appears as `/example.com/video/123` in the redirect URI if `example.com` is the hostname
           in the incoming HTTP request URI.

        *  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and
           `123` is the port in the incoming HTTP request URI.

        *  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP
           request URI.


        :param path: The path of this RedirectUri.
        :type: str
        """
        self._path = path

    @property
    def query(self):
        """
        Gets the query of this RedirectUri.
        The query string to use in the redirect URI.

        When this value is null, not set, or set to `{query}`, the service preserves the original query parameters
        from the incoming HTTP request URI.

        All `RedirectUri` tokens are valid for this property. You can use any token more than once.

        If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.

        You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand
        (&) character. To omit all incoming query parameters from the redirect URI, set this value to an empty
        string, \"\".

        If the specified query string results in a redirect URI ending with `?` or `&`, the last character is truncated.
        For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is
        `?lang=en&{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system
        truncates the final ampersand (&) because the incoming URI included no value to replace the {query} token.

        Examples:
        * **lang=en&time_zone=PST** appears as `lang=en&time_zone=PST` in the redirect URI.

        * **{query}** appears as `lang=en&time_zone=PST` in the redirect URI if `lang=en&time_zone=PST` is the query
          string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}`
          token renders as an empty string.

        * **lang=en&{query}&time_zone=PST** appears as `lang=en&country=us&time_zone=PST` in the redirect URI if
          `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query
          parameters, this value renders as `lang=en&time_zone=PST`.

        *  **protocol={protocol}&hostname={host}** appears as `protocol=http&hostname=example.com` in the redirect
           URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request.

        *  **port={port}&hostname={host}** appears as `port=8080&hostname=example.com` in the redirect URI if the
           port is `8080` and the hostname is `example.com` in the incoming HTTP request URI.


        :return: The query of this RedirectUri.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this RedirectUri.
        The query string to use in the redirect URI.

        When this value is null, not set, or set to `{query}`, the service preserves the original query parameters
        from the incoming HTTP request URI.

        All `RedirectUri` tokens are valid for this property. You can use any token more than once.

        If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.

        You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand
        (&) character. To omit all incoming query parameters from the redirect URI, set this value to an empty
        string, \"\".

        If the specified query string results in a redirect URI ending with `?` or `&`, the last character is truncated.
        For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is
        `?lang=en&{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system
        truncates the final ampersand (&) because the incoming URI included no value to replace the {query} token.

        Examples:
        * **lang=en&time_zone=PST** appears as `lang=en&time_zone=PST` in the redirect URI.

        * **{query}** appears as `lang=en&time_zone=PST` in the redirect URI if `lang=en&time_zone=PST` is the query
          string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}`
          token renders as an empty string.

        * **lang=en&{query}&time_zone=PST** appears as `lang=en&country=us&time_zone=PST` in the redirect URI if
          `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query
          parameters, this value renders as `lang=en&time_zone=PST`.

        *  **protocol={protocol}&hostname={host}** appears as `protocol=http&hostname=example.com` in the redirect
           URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request.

        *  **port={port}&hostname={host}** appears as `port=8080&hostname=example.com` in the redirect URI if the
           port is `8080` and the hostname is `example.com` in the incoming HTTP request URI.


        :param query: The query of this RedirectUri.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

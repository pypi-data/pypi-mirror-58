# -*- coding: utf-8 -*-
#
# Copyright 2019 ITRS Group Ltd. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import os
from .api import Api
from .senders import StatsdMetricsSender
from .channels import UdpChannel, TcpChannel, StdoutChannel

DEFAULT_STATSD_SERVER = 'localhost'
DEFAULT_STATSD_PORT = 8125
PROTO_TCP = 'tcp'
PROTO_UDP = 'udp'
ENV_DIMENSION_PREFIX = 'STATSD_DIMENSION_'

platform_dimensions_kubernetes = {
    'NAMESPACE': 'namespace',
    'POD_NAME': 'pod_name',
    'CONTAINER_NAME': 'container_name',
    'HOSTNAME': 'hostname'
}

platform_dimensions_default = {
    'APP_NAME': 'app_name',
    'HOSTNAME': 'hostname'
}


def build_statsd(**kwargs):
    """Build a statsd API client.

    The client can be configured via environment variables and/or method arguments.  The environment
    variables, which have precedence over the method arguments, are as follows:

    | STATSD_SERVER: server address
    | STATSD_PORT:  server port
    | STATSD_PROTOCOL:  tcp or udp (default)
    | STATSD_DIMENSION_<name>:  custom dimension(s)
    | STATSD_DISABLE_PLATFORM_DIMENSIONS: true|false

    :param kwargs: (optional) Set 'hostname' and 'port' to override the default of localhost:8125.
        If 'protocol' is supplied, it will override the default of UDP (valid values are 'tcp' and 'udp').
        To disable automatic platform dimensions, set 'disable_platform_dimensions' to True.
    :return: :class:`Api`
    :rtype: itrsstatsd.Api
    :raises: ValueError if unknown protocol specified
    """

    hostname = os.environ.get('STATSD_SERVER', kwargs.get('hostname', DEFAULT_STATSD_SERVER))
    port = int(os.environ.get('STATSD_PORT', kwargs.get('port', DEFAULT_STATSD_PORT)))
    protocol = os.environ.get('STATSD_PROTOCOL', kwargs.get('protocol', PROTO_UDP))

    if PROTO_TCP == protocol:
        channel = TcpChannel(hostname, port)
    elif PROTO_UDP == protocol:
        channel = UdpChannel(hostname, port)
    else:
        raise ValueError('Unknown protocol: ' + protocol)

    return _build(channel, **kwargs)


def _build(channel, **kwargs):
    api = Api(StatsdMetricsSender(channel))
    env = os.environ.get('STATSD_DISABLE_PLATFORM_DIMENSIONS', None)

    if env is None:
        if not kwargs.get('disable_platform_dimensions', False):
            _add_platform_dimensions(api)
    elif env != 'true':
        _add_platform_dimensions(api)

    _add_env_dimensions(api)
    return api


def _add_platform_dimensions(api: Api):
    if os.environ.get('POD_NAME', None) is not None:
        dims = platform_dimensions_kubernetes
    else:
        dims = platform_dimensions_default

    for env_name, dimension_name in dims.items():
        env_value = os.environ.get(env_name, None)
        if env_value is not None:
            api.default_dimension(dimension_name, env_value)

    return api


def _add_env_dimensions(api: Api):
    for k in os.environ:
        if k.startswith(ENV_DIMENSION_PREFIX):
            api.default_dimension(k[len(ENV_DIMENSION_PREFIX):], os.environ.get(k))


def build_test_statsd(**kwargs):
    """Build a test statsd API client.

    A test statsd API client simply outputs statsd packets to stdout rather than to a statsd server.

    :return: :class:`Api`
    :rtype: itrsstatsd.Api
    """

    return _build(StdoutChannel(), **kwargs)

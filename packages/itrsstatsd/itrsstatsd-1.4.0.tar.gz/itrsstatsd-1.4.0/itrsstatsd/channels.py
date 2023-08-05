# -*- coding: utf-8 -*-
#
# Copyright 2019 ITRS Group Ltd. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import socket
import time


class StdoutChannel:

    def connect(self):
        pass

    @staticmethod
    def send(message):
        print(message)

    def close(self):
        pass


class RecordingChannel:

    def __init__(self, slow=False):
        self._messages = []
        self._slow = slow

    def connect(self):
        pass

    def send(self, message):
        if self._slow:
            time.sleep(5)
        self._messages.append(message)

    def close(self):
        pass

    def get_messages(self):
        return self._messages


class UdpChannel:

    def __init__(self, hostname, port):
        self._port = port
        self._hostname = hostname
        self._socket = None

    def connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        sock = self._socket
        if sock is not None:
            sock.sendto(bytes(message + '\n', 'UTF-8'), (self._hostname, self._port))

    def close(self):
        sock = self._socket
        if sock is not None:
            sock.close()


class TcpChannel:

    def __init__(self, hostname, port):
        self._port = port
        self._hostname = hostname
        self._socket = None

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(15)
        sock.connect((self._hostname, self._port))
        self._socket = sock

    def send(self, message):
        sock = self._socket
        if sock is not None:
            sock.send(bytes(message + '\n', 'UTF-8'))

    def close(self):
        sock = self._socket
        if sock is not None:
            sock.close()
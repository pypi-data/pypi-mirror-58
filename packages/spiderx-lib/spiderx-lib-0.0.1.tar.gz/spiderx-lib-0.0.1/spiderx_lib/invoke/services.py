# coding=utf-8
from typing import Dict, Any

import grpc

from spiderx_lib.log import service_log
from .task import TaskService


class GrpcServiceManager(object):
    def __init__(self, options: Dict[str, Any] = None):
        self._channel = None
        self._options: Dict[str, Any] = options
        if options is not None:
            self.open_channel(options=options)

        # 所有的service
        self.task_service: TaskService = None

    def open_channel(self, options: Dict[str, Any], init_service: bool = True):
        self._options = options
        self._channel = grpc.insecure_channel(self._options['GRPC_URI'])

        if init_service:
            self._init_services()

    def close_channel(self):
        service_log.debug("close channel")
        if self._channel:
            self._channel.close()

    def _init_services(self):
        # 初始化所有的service
        self.task_service = TaskService(channel=self._channel)

    def reconnect(self):
        self.close_channel()
        self.open_channel(options=self._options)

    def __del__(self):
        self.close_channel()


grpc_service = GrpcServiceManager()

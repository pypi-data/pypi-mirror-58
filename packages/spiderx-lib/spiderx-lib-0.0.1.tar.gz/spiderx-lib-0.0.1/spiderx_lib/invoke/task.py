# coding=utf-8
from spiderx_lib.invoke.gen import task_pb2_grpc, task_pb2
from spiderx_lib.log import service_log


class TaskService(object):
    def __init__(self, channel):
        self._channel = channel
        self.stub = task_pb2_grpc.TaskServiceStub(channel=channel)
        service_log.debug("init task service success.")

    # 定义几个行为
    def send_task(
            self,
            policy: str,
            url: str,
            site_name: str,
            depth: int,
            father: str,
            task_type: str,
            message: str
    ):
        """
        表示发送任务，去重
        :return:
        """
        req = task_pb2.SendTaskRequest(
            policy=policy,
            url=url,
            site_name=site_name,
            depth=depth,
            father=father,
            task_type=task_type,
            dont_filter=False,
            message=message
        )
        return self.stub.SendTaskByClient(req, timeout=10)

    def start_task(
            self,
            policy: str,
            url: str,
            site_name: str,
            depth: int,
            father: str,
            task_type: str,
            message: str
    ):
        """
        表示不去重，直接发到队列
        :return:
        """
        req = task_pb2.SendTaskRequest(
            policy=policy,
            url=url,
            site_name=site_name,
            depth=depth,
            father=father,
            task_type=task_type,
            dont_filter=True,
            message=message
        )
        return self.stub.SendTaskByClient(req, timeout=10)

    def finish_task(
            self,
            task_id: str,
            stat: str,
            message: str,
    ):
        """
        完成任务
        :return:
        """

        req = task_pb2.SendTaskRequest(
            task_id=task_id,
            stat=stat,
            message=message
        )
        return self.stub.SendTaskByClient(req, timeout=10)

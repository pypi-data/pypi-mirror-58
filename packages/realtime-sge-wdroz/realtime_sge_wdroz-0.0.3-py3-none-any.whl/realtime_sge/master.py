""" master who control slaves
"""
import datetime
import time
from pprint import pprint
import grpc
from concurrent import futures
from realtime_sge.protos import services_pb2_grpc
from realtime_sge.protos.messages_pb2 import Empty, Action, Command
from itertools import cycle


class WorkerHandler(object):
    def __init__(self, worker_id, host, port, status_delay_s=3):
        self._worker_id = worker_id
        self._host = host
        self._port = port
        self._lastnew = datetime.datetime.now()
        self._ram_usage = 0.0
        self._cpu_usage = 0.0
        self._status_delay_s = status_delay_s
        self._channel = grpc.insecure_channel("{}:{}".format(host, port))
        self._stub = services_pb2_grpc.SlaveStub(self._channel)

    def update_status(self):
        status = self._stub.GetStatus(Empty())
        self._ram_usage = status.ram_usage
        self._cpu_usage = status.cpu_usage
        self._lastnew = datetime.datetime.now()

    def kill(self):
        self._stub.DoCommand(Command(action=Action.QUIT))
        self._channel.close()

    def __str__(self):
        return "{}  - RAM({:.2f}%) CPU({:.2f}%)".format(
            self._worker_id, self._ram_usage, self._cpu_usage
        )

    def __repr__(self):
        return str(self)

    def compute_task(self, task):
        return self._stub.DoTask.future(task)


class Master(services_pb2_grpc.MasterServicer):
    def __init__(self):
        super().__init__()
        self._slaves = dict()

    def Register(self, request, context):
        worker_handler = WorkerHandler(
            worker_id=request.id, host=request.host, port=request.port
        )
        self._slaves[request.id] = worker_handler
        return Empty()

    def print(self):
        print("### {:03d} slaves ###".format(len(self._slaves)))
        pprint(self._slaves)
        print("-" * 20)

    def kill(self):
        for worker_handler in self._slaves.values():
            worker_handler.kill()

        self._slaves = dict()

    def update(self):
        for worker_handler in self._slaves.values():
            worker_handler.update_status()

    def compute_tasks(self, task_list, ReplyClass):
        future_results = []
        for task, worker in zip(task_list, cycle(self._slaves.keys())):
            future_results.append(self._slaves[worker].compute_task(task))

        results = []
        for future_result in future_results:
            reply = ReplyClass()
            reply.MergeFromString(future_result.result().SerializeToString())
            results.append(reply)

        return results


def create_master_server(master_host="[::]", master_port=1234):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    master = Master()
    services_pb2_grpc.add_MasterServicer_to_server(master, server)
    server.add_insecure_port("{}:{}".format(master_host, master_port))
    return master, server


def serve_master(master, server):

    server.start()
    while True:
        try:
            master.update()
            master.print()
        except KeyboardInterrupt:
            master.kill()
            server.stop(grace=0)
            exit(0)


if __name__ == "__main__":
    master, server = create_master_server()
    serve_master(master, server)

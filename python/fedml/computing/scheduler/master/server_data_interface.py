
import os
import sqlite3

from fedml.computing.scheduler.master.server_constants import ServerConstants
from fedml.computing.scheduler.slave.client_data_interface import FedMLClientDataInterface


class FedMLServerDataInterface(FedMLClientDataInterface):
    # TODO(fedml-alex,fedml-dimitris): Refactoring suggestion, rename 
    # `FedMLClientDataInterface` to `FedMLDataInterface` move into comm_utils
    # and materialize the interface inside server and client packages, or simply 
    # move `FedMLDataInterface` into comm_utils and create an object when needed.
    MAX_JOB_LIST_SIZE = 50000
    ERRCODE_JOB_FAILED = 1
    ERRCODE_JOB_KILLED = 2

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        return FedMLServerDataInterface()

    # TODO(fedml-alex,fedml-dimitris): The following function is identical to
    # the open_job_db() function declare in:
    # python/fedml/computing/scheduler/slave/client_data_interface.py#L118
    # we can safely remove this.
    def open_job_db(self):
        if not os.path.exists(ServerConstants.get_database_dir()):
            os.makedirs(ServerConstants.get_database_dir(), exist_ok=True)
        job_db_path = os.path.join(ServerConstants.get_database_dir(), "jobs.db")
        self.db_connection = sqlite3.connect(job_db_path)



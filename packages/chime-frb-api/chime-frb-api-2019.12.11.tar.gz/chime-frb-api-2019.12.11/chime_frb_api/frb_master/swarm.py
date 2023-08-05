#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chime_frb_api.core import API
import typing as t
import logging
from time import sleep

log = logging.getLogger(__name__)
JSON = t.Union[str, int, float, bool, None, t.Mapping[str, "JSON"], t.List["JSON"]]
JOBS = t.List[str]


class Swarm(object):
    """
    CHIME/FRB Swarm API

    Parameters
    ----------
    API : chime_frb_api.core.API class-type
    """

    def __init__(self, API: API):
        self.API = API

    def get_jobs(self) -> JSON:
        """
        Returns the name of all jobs on the analysis cluster.
        """
        return self.API.get(url="/v1/swarm/jobs")

    def get_job_status(self, job_name: str) -> JSON:
        """
        Get job[s] status with a regex match to argument job_name

        Parameters
        ----------
        job_name : str
            Name of the job

        Returns
        -------
        { job_name : STATUS } : dict

            Where STATUS can be,
            NEW         The job was initialized.
            PENDING     Resources for the job were allocated.
            ASSIGNED    Docker assigned the job to nodes.
            ACCEPTED    The job was accepted by a worker node.
            PREPARING   Docker is preparing the job.
            STARTING    Docker is starting the job.
            RUNNING     The job is executing.
            COMPLETE    The job exited without an error code.
            FAILED      The job exited with an error code.
            SHUTDOWN    Docker requested the job to shut down.
            REJECTED    The worker node rejected the job.
            ORPHANED    The node was down for too long.
            REMOVE      The job is not terminal but the associated job was removed
        """
        return self.API.get("/v1/swarm/job-status/{}".format(job_name))

    def spawn_job(
        self,
        image_name: str,
        command: list,
        arguments: list,
        job_name: str,
        mount_archiver: bool = True,
        swarm_network: bool = True,
        job_mem_limit: int = 4294967296,
        job_mem_reservation: int = 268435456,
        job_cpu_limit: float = 1,  # 1 Core Max
        job_cpu_reservation: float = 1,  # 0.1 Core Reserved
        environment: dict = {},
    ) -> JSON:
        """
        Spawn a job on the CHIME/FRB Analysis Cluster

        Parameters
        ----------

        image_name : str
            Name of the container image to spawn the job with
            e.g. chimefrb/iautils:latest

        command : list
            The command to be run in the container

        arguments : list
            Arguments to the command

        job_name : string
            Unique name for the cluster job

        mount_archiver : bool
            Mount Site Data Archivers

        swarm_network : bool
            Mount Cluster Network

        job_mem_limit : int
            Represents the memory limit of the created container in bytes

        job_mem_reservation : int
            Represents the minimum memory reserved of the created container in bytes

        job_cpu_limit : float
            Represents maximum cpu cores assigned to the job, default is 1

        job_cpu_reservation : float
            Represents minimum cpu cores needed to start the job, default is 0.1

        environment : dict
            ENV variables to pass to the container, e.g FRB_MASTER_USERNAME="shiny"

        Returns
        -------
        result : dict
        """
        payload = {
            "image_name": image_name,
            "command": command,
            "arguments": arguments,
            "job_name": job_name,
            "mount_archiver": mount_archiver,
            "swarm_network": swarm_network,
            "job_mem_reservation": job_mem_reservation,
            "job_mem_limit": job_mem_limit,
            "job_cpu_limit": job_cpu_limit,
            "job_cpu_reservation": job_cpu_reservation,
            "environment": environment,
        }
        return self.API.post(url="/v1/swarm/spawn-job", json=payload)

    def get_logs(self, job_name: str) -> JSON:
        """
        Return logs from a CHIME/FRB Job

        Parameters
        ----------
        job_name : string
            Unique name for the cluster job

        Returns
        -------
            job_logs : dict
        """
        return self.API.get("/v1/swarm/logs/{}".format(job_name))

    def prune_jobs(self, job_name: str) -> JSON:
        """
        Remove COMPLETED jobs with a regex match to argument job_name

        Parameters
        ----------
        job_name : string
            Unique name for the cluster job

        Returns
        -------
            dict: {job_name : boolean}
        """
        return self.API.get(url="/v1/swarm/prune-job/{}".format(job_name))

    def kill_job(self, job_name: str) -> JSON:
        """
        Remove (forcibly) job with ANY status but with an exact match to job_name

        Parameters
        ----------
        job_name : string
            Unique name for the cluster job

        Returns
        -------
            dict: {job_name : boolean}
        """
        return self.API.get(url="/v1/swarm/kill-job/{}".format(job_name))

    def kill_failed_jobs(self, job_name: str = None) -> JSON:
        """
        Remove FAILED jobs with a regex match to job_name

        Parameters
        ----------
        job_name : string
            Unique name for the cluster job

        Returns
        -------
            dict: {job_name : boolean}
        """
        assert isinstance(job_name, str), "job_name <str> is required"
        status = {}
        for job in self.get_jobs():
            if job_name in job:
                if self.get_job_status(job)[job] == "failed":
                    status[job] = self.kill_job(job)[job]
        return status

    def jobs_running(self, job_names: t.List[str]) -> bool:
        """
        Monitors job[s] on the CHIME/FRB Analysis Cluster untill they are either
        COMPLETE, FAILED or SHUTDOWN

        Parameters
        ----------
        job_names : list
            A list of string job_name paramerters to monitor
        """
        running_statuses = [
            "new",
            "pending",
            "assigned",
            "accepted",
            "preparing",
            "starting",
            "running",
        ]
        if isinstance(job_names, str):
            job_names = [job_names]
        jobs_status = {}
        for job in job_names:
            status = self.get_job_status(job)
            jobs_status[job] = status
            for running in running_statuses:
                if running in status.values():
                    return True
        return False

    def monitor_jobs(self, job_name: t.List[str], error_logs: bool = False) -> dict:
        """
        Continously monitor job[s] on the CHIME/FRB Analysis Cluster

        Parameters
        ----------
        job_name : str
            Regular expression matching to the job_name

        Returns
        -------
        status : bool
            Status of the pipeline
        """
        log.info("================================================")
        log.info("Monitoring Pipeline: {}".format(job_name))
        log.info("================================================")
        initiating = ["new", "accepted", "pending", "starting", "preparing", "assigned"]
        status = self.get_job_status(job_name)
        while any([n in initiating for n in status.values()]):
            sleep(30)
            status = self.get_job_status(job_name)
        # Initiation
        log.info("Pipeline Initiation: Complete")
        log.info("================================================")
        log.info("Pipeline Processing: Started")
        status = self.get_job_status(job_name)
        while "running" in status.values():
            log.info("Pipeline Processing: Running")
            sleep(120)
            status = self.get_job_status(job_name)
        log.info("Pipeline Processing: Complete")
        log.info("================================================")
        log.info("Pipeline Completion Status")
        completed = failed = 0
        for key, value in status.items():
            if value == "completed":
                completed += 1
            else:
                failed += 1
        log.info("Completed : {}%".format((completed / len(status)) * 100))
        log.info("Failed    : {}%".format((failed / len(status)) * 100))
        log.info("================================================")
        log.info("Pipeline Cleanup: Started")
        self.prune_jobs(job_name)
        # Make sure all jobs were pruned, if not report and kill them
        # TODO: In the future respawn "failed" jobs
        status = self.get_job_status(job_name)
        if len(status.keys()) > 0:
            log.error("Pipeline Cleanup: Failed Jobs Detected")
            for job in status.keys():
                log.error("Job Name : {}".format(key))
                log.error("Job Removal: {}".format(self.kill_job(job)))
            log.info("Pipeline Cleanup: Completed with Failed Jobs")
            return False
        log.info("Pipeline Cleanup: Completed")
        log.info("================================================")
        return True

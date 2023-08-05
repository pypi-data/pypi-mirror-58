from datetime import datetime
from uuid import UUID
from typing import Union
from dateutil.parser import parse

from datalogue.utils import SerializableStringEnum
from datalogue.errors import _enum_parse_error, DtlError


class JobStatus(SerializableStringEnum):
    Scheduled = "Scheduled"
    Defined = "Defined"
    Running = "Running"
    Succeeded = "Succeeded"
    Failed = "Failed"
    Unknown = "Unknown"

    @staticmethod
    def parse_error(s: str) -> str:
        return _enum_parse_error("job status", s)


def job_status_from_str(string: str) -> Union[DtlError, JobStatus]:
    return SerializableStringEnum.from_str(JobStatus)(string)


class Job:
    def __init__(self, job_id: UUID, run_at: datetime, status: JobStatus, workflow_id: UUID):
        self.id = job_id
        self.workflow_id = workflow_id
        self.status = status
        self.run_at = run_at


def _job_from_payload(json: dict) -> Union[DtlError, Job]:
    job_id = json.get("id")
    if job_id is None:
        return DtlError("Job object should have an 'id' property")
    else:
        try:
            job_id = UUID(job_id)
        except ValueError:
            return DtlError("'id' field was not a proper uuid")

    run_at = json.get("runDate")
    if run_at is None:
        return DtlError("Job object should have a 'runDate' property")
    else:
        try:
            run_at = parse(run_at)
        except ValueError:
            return DtlError("The 'runDate' could not be parsed as a valid date")

    status = json.get("combinedStreamState")
    if status is None:
        return DtlError("Job object should have a 'combinedStreamState' property")
    else:
        status = job_status_from_str(status)
        if isinstance(status, DtlError):
            return status

    workflow_id = json.get("workflowId")
    if workflow_id is None:
        return DtlError("Job object should have a 'workflowId' property")
    else:
        try:
            workflow_id = UUID(workflow_id)
        except ValueError:
            return DtlError("'workflowId' field was not a proper uuid")

    return Job(job_id, run_at, status, workflow_id)

"""Stream type classes for tap-greenhouse."""

from __future__ import annotations

from tap_greenhouse import schemas
from tap_greenhouse.client import GreenhouseStream


class ListCandidatesStream(GreenhouseStream):
    """List Candidates stream."""

    name = "list_candidates"
    path = "candidates"
    primary_keys = ["id"]
    replication_key = "last_activity"
    schema = schemas.candidates


class ListApplicationsStream(GreenhouseStream):
    """List Applications stream."""

    name = "list_applications"
    path = "applications"
    primary_keys = ["id"]
    replication_key = "last_activity_at"
    schema = schemas.applications


class ListJobsStream(GreenhouseStream):
    """List Jobs Stream."""

    name = "list_jobs"
    path = "jobs"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.jobs

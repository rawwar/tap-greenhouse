"""Stream type classes for tap-greenhouse."""

from __future__ import annotations

from tap_greenhouse import schemas
from tap_greenhouse.client import GreenhouseStream


class ListCandidateStream(GreenhouseStream):
    """Define custom stream."""

    name = "list_candidates"
    path = "candidates"
    primary_keys = ["id"]
    replication_key = "last_activity"
    schema = schemas.candidates

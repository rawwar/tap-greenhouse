"""Making it easy to import all Schemas."""
from .activity_feed import schema_dict as activity_feed
from .applications import schema_dict as applications
from .candidates import schema_dict as candidates
from .job_openings import schema_dict as job_openings
from .jobs import schema_dict as jobs

__all__ = ["candidates", "applications", "jobs", "job_openings", "activity_feed"]

"""Making it easy to import all Schemas."""
from .applications import schema_dict as applications
from .candidates import schema_dict as candidates
from .jobs import schema_dict as jobs

__all__ = ["candidates", "applications", "jobs"]

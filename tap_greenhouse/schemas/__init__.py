"""Making it easy to import all Schemas."""
from .activity_feed import schema_dict as activity_feed
from .applications import schema_dict as applications
from .approval_flows import schema_dict as approval_flows
from .candidates import schema_dict as candidates
from .close_reasons import schema_dict as close_reasons
from .custom_fields import schema_dict as custom_fields
from .departments import schema_dict as departments
from .eeoc import schema_dict as eeoc
from .job_openings import schema_dict as job_openings
from .job_posts import schema_dict as job_posts
from .job_stages import schema_dict as job_stages
from .jobs import schema_dict as jobs
from .list_approvals import schema_dict as list_approvals
from .list_demographic_questions import schema_dict as list_demographic_questions
from .offer import schema_dict as offer
from .pending_approvals_for_user import schema_dict as pending_approvals_for_user

__all__ = [
    "activity_feed",
    "applications",
    "approval_flows",
    "candidates",
    "close_reasons",
    "job_openings",
    "jobs",
    "list_approvals",
    "pending_approvals_for_user",
    "custom_fields",
    "list_demographic_questions",
    "departments",
    "eeoc",
    "job_posts",
    "job_stages",
    "offer",
]

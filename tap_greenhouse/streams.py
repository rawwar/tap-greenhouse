"""Stream type classes for tap-greenhouse."""
# ruff: noqa: ARG002

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

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "candidate_id": record["id"],
        }


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

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "job_id": record["id"],
        }


class ListJobOpeningStream(GreenhouseStream):
    """List Job Opening Stream."""

    name = "list_job_openings"
    parent_stream_type = ListJobsStream
    ignore_parent_replication_key = True
    path = "jobs/{job_id}/openings"
    schema = schemas.job_openings


class ActivityFeedStream(GreenhouseStream):
    """Candidate Activity feed stream."""

    name = "activity_feed"
    parent_stream_type = ListCandidatesStream
    ignore_parent_replication_key = True
    path = "candidates/{candidate_id}/activity_feed"
    schema = schemas.activity_feed


class ListApprovalsStream(GreenhouseStream):
    """List Approvals for a job."""

    name = "list_approvals"
    parent_stream_type = ListJobsStream
    ignore_parent_replication_key = True
    path = "jobs/{job_id}/approval_flows"
    schema = schemas.list_approvals

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "id": record["id"],
        }


class ApprovalFlowStream(GreenhouseStream):
    """Get: Retrieve Approval Flow."""

    name = "retrieve_approval_flow"
    parent_stream_type = ListApprovalsStream
    ignore_parent_replication_key = True
    path = "approval_flows/{id}"
    schema = schemas.approval_flows


class ListUsersStream(GreenhouseStream):
    """List Users Stream."""

    name = "list_users"
    path = "users"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.users

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "user_id": record["id"],
        }


class PendingApprovalsForUserStream(GreenhouseStream):
    """List Pending Approvals for user Stream."""

    name = "pending_approvals_for_user"
    parent_stream_type = ListUsersStream
    ignore_parent_replication_key = True
    path = "users/{user_id}/pending_approvals"
    schema = schemas.pending_approvals_for_user


class ListCloseReasonStream(GreenhouseStream):
    """Close Reasons Stream."""

    name = "list_close_reason"
    path = "close_reasons"
    schema = schemas.close_reasons


class ListCustomFieldStream(GreenhouseStream):
    """Custom Fields Stream."""

    name = "list_custom_field"
    path = "custom_fields"
    schema = schemas.custom_fields


class ListDemographicQuestionStream(GreenhouseStream):
    """List Demographic Question Stream."""

    name = "list_demographic_question"
    path = "demographics/questions"
    primary_keys = ["id"]
    schema = schemas.list_demographic_questions


class ListDepartmentStream(GreenhouseStream):
    """Department Stream."""

    name = "list_department"
    path = "departments"
    primary_keys = ["id"]
    schema = schemas.departments


class ListEEOCStream(GreenhouseStream):
    """List EEOC Stream."""

    name = "list_eeoc"
    path = "eeoc"
    primary_keys = ["application_id"]
    schema = schemas.eeoc


class ListJobPostStream(GreenhouseStream):
    """Job Post Stream."""

    name = "list_job_post"
    path = "job_posts"
    primary_keys = ["id"]
    schema = schemas.job_posts


class ListJobStageStream(GreenhouseStream):
    """Job Stage Stream."""

    name = "list_job_stage"
    path = "job_stages"
    primary_keys = ["id"]
    schema = schemas.job_stages


class ListOfferStream(GreenhouseStream):
    """Offer Stream."""

    name = "list_offer"
    path = "offers"
    primary_keys = ["id"]
    schema = schemas.offer


class ListOfficeStream(GreenhouseStream):
    """Office Stream."""

    name = "list_office"
    path = "offices"
    primary_keys = ["id"]
    schema = schemas.offices


class ListProspectPoolsStream(GreenhouseStream):
    """List Prospect Pools stream."""

    name = "list_prospect_pools"
    path = "prospect_pools"
    primary_keys = ["id"]
    schema = schemas.prospect_pools


class ListRejectionReasonStream(GreenhouseStream):
    """Rejection Reasons Stream."""

    name = "list_rejection_reason"
    path = "rejection_reasons"
    primary_keys = ["id"]
    schema = schemas.rejection_reasons


class ListScheduledInterviewStream(GreenhouseStream):
    """Scheduled Interviews Stream."""

    name = "list_scheduled_interview"
    path = "scheduled_interviews"
    primary_keys = ["id"]
    schema = schemas.scheduled_interviews


class ListScorecardStream(GreenhouseStream):
    """Scorecard Stream."""

    name = "list_scorecard"
    path = "scorecards"
    primary_keys = ["id"]
    schema = schemas.list_scorecards


class ListSourceStream(GreenhouseStream):
    """Sources Stream."""

    name = "list_source"
    path = "sources"
    primary_keys = ["id"]
    schema = schemas.list_sources


class ListCandidateTagStream(GreenhouseStream):
    """Candidate Tag Stream."""

    name = "list_candidate_tag"
    path = "tags/candidate"
    primary_keys = ["id"]
    schema = schemas.tags


class ListUserJobPermissionsStream(GreenhouseStream):
    """List user job permissions Stream."""

    name = "list_user_job_permissions"
    parent_stream_type = ListUsersStream
    ignore_parent_replication_key = True
    path = "users/{user_id}/permissions/jobs"
    schema = schemas.user_permissions


class UserRoleStream(GreenhouseStream):
    """User Roles Stream."""

    name = "user_role"
    path = "user_roles"
    schema = schemas.user_role

"""greenhouse tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_greenhouse import streams


class Tapgreenhouse(Tap):
    """greenhouse tap class."""

    name = "tap-greenhouse"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://harvest.greenhouse.io/v1/",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.GreenhouseStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ListCandidatesStream(self),
            streams.ListApplicationsStream(self),
            streams.ListJobsStream(self),
            streams.ActivityFeedStream(self),
            streams.ListApprovalsStream(self),
            streams.ApprovalFlowStream(self),
            streams.ListUsersStream(self),
            streams.PendingApprovalsStream(self),
            streams.PendingApprovalsForUserStream(self),
            streams.ListCloseReasonStream(self),
            streams.ListCustomFieldStream(self),
            streams.ListDemographicQuestionStream(self),
            streams.ListDepartmentStream(self),
            streams.ListEEOCStream(self),
            streams.ListJobPostStream(self),
            streams.ListJobStageStream(self),
            streams.ListOfferStream(self),
            streams.ListOfficeStream(self),
            streams.ListProspectPoolsStream(self),
            streams.ListRejectionReasonStream(self),
            streams.ListScheduledInterviewStream(self),
            streams.ListScorecardStream(self),
            streams.ListSourceStream(self),
            streams.ListCandidateTagStream(self),
            streams.ListUserJobPermissionsStream(self),
            streams.UserRoleStream(self),
        ]


if __name__ == "__main__":
    Tapgreenhouse.cli()

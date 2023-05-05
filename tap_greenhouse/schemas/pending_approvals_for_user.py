"""Singer schema for Pending Approvals for User endpoint."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("status", th.StringType),
    th.Property("created_at", th.StringType),
    th.Property("resolved_at", th.NullableType(th.StringType)),
    th.Property("request_sent_at", th.StringType),
    th.Property("reminder_sent_at", th.StringType),
    th.Property("reminders_sent", th.IntegerType),
    th.Property("approver_group_id", th.IntegerType),
    th.Property("reminder_sent_by_user_id", th.IntegerType),
    th.Property("hiring_plan_id", th.IntegerType),
    th.Property("offer_id", th.NullableType(th.IntegerType)),
    th.Property("approval_flow_id", th.IntegerType),
    th.Property("approval_flow_type", th.StringType),
    th.Property("approval_flow_status", th.StringType),
)

schema_dict = schema.to_dict()

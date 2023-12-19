"""JSON Schemas for Scheduled Interviews stream."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("application_id", th.IntegerType),
    th.Property("external_event_id", th.StringType),
    th.Property(
        "start",
        th.ObjectType(
            th.Property("date_time", th.DateTimeType),
        ),
    ),
    th.Property(
        "end",
        th.ObjectType(
            th.Property("date_time", th.DateTimeType),
        ),
    ),
    th.Property("location", th.StringType),
    th.Property("video_conferencing_url", th.StringType),
    th.Property("status", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property(
        "interview",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "organizer",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("name", th.StringType),
            th.Property("employee_id", th.StringType),
        ),
    ),
    th.Property(
        "interviewers",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("employee_id", th.StringType),
                th.Property("name", th.StringType),
                th.Property("email", th.StringType),
                th.Property("response_status", th.StringType),
                th.Property("scorecard_id", th.IntegerType),
            ),
        ),
    ),
)


schema_dict = schema.to_dict()

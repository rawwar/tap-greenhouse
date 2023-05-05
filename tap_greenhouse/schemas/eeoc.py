"""JSON Schemas for EEOC."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("application_id", th.IntegerType),
    th.Property("candidate_id", th.IntegerType),
    th.Property(
        "race",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("description", th.StringType),
        ),
    ),
    th.Property(
        "gender",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("description", th.StringType),
        ),
    ),
    th.Property(
        "veteran_status",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("message", th.StringType),
        ),
    ),
    th.Property(
        "disability_status",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("description", th.StringType),
        ),
    ),
    th.Property("submitted_at", th.DateTimeType),
)

schema_dict = schema.to_dict()

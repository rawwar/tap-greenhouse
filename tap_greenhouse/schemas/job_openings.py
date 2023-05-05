"""Job Opening Schema."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("opening_id", th.StringType),
    th.Property("status", th.StringType),
    th.Property("opened_at", th.DateTimeType),
    th.Property("closed_at", th.DateTimeType),
    th.Property("application_id", th.IntegerType),
    th.Property(
        "close_reason",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property("custom_fields", th.ObjectType()),
    th.Property("keyed_custom_fields", th.ObjectType()),
)

schema_dict = schema.to_dict()

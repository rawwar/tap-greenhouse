"""Singer schema for Greenhouse Close Reasons."""
from singer_sdk import typing as th

schema = th.ListType(
    th.ObjectType(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
    ),
)

schema_dict = schema.to_dict()

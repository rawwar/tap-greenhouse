"""Schema for user role stream."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("type", th.StringType),
    th.Property("name", th.StringType),
)

schema_dict = schema.to_dict()

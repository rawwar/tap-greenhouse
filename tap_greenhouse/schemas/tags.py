"""Schema for tags."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
)

schema_dict = schema.to_dict()

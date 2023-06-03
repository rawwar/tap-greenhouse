"""Singer schema for Greenhouse Close Reasons."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
)

schema_dict = schema.to_dict()

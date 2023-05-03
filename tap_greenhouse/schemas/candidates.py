"""Candidates Schema."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("company", th.StringType),
    th.Property("last_activity", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
).to_dict()

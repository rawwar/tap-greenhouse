"""Schema for user permissions stream."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("job_id", th.IntegerType),
    th.Property("user_role_id", th.IntegerType),
)

schema_dict = schema.to_dict()

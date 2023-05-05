"""JSON Schema for Greenhouse API: List Demographic Questions."""
from singer_sdk import typing as th

schema = th.ArrayType(
    th.ObjectType(
        th.Property("id", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("description", th.StringType),
        th.Property("active", th.BooleanType),
    ),
)

schema_dict = schema.to_dict()

"""Singer schema for Prospect Pools."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("active", th.BooleanType),
    th.Property(
        "prospect_stages",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()

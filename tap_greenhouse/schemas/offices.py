"""JSON Schema for Greenhouse Offices."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property(
        "location",
        th.PropertiesList(
            th.Property("name", th.StringType),
        ),
    ),
    th.Property("primary_contact_user_id", th.IntegerType),
    th.Property("parent_id", th.IntegerType),
    th.Property("parent_office_external_id", th.StringType),
    th.Property("child_ids", th.ArrayType(th.IntegerType)),
    th.Property("child_office_external_ids", th.ArrayType(th.StringType)),
    th.Property("external_id", th.StringType),
)

schema_dict = schema.to_dict()

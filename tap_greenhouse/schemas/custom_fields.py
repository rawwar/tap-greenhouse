"""Singer schema for Greenhouse custom fields."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("active", th.BooleanType),
    th.Property("field_type", th.StringType),
    th.Property("priority", th.IntegerType),
    th.Property("value_type", th.StringType),
    th.Property("private", th.BooleanType),
    th.Property("required", th.BooleanType),
    th.Property("require_approval", th.BooleanType),
    th.Property("trigger_new_version", th.BooleanType),
    th.Property("name_key", th.StringType),
    th.Property("description", th.StringType),
    th.Property("expose_in_job_board_api", th.BooleanType),
    th.Property("api_only", th.BooleanType),
    th.Property(
        "offices",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
    ),
    th.Property(
        "departments",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
    ),
    th.Property("template_token_string", th.StringType),
    th.Property(
        "custom_field_options",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("priority", th.IntegerType),
                th.Property(
                    "external_id",
                    th.StringType,
                    required=False,
                ),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()

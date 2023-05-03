"""Candidates Schema."""
from singer_sdk import typing as th

from tap_greenhouse.schemas.applications import schema as application_schema

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("company", th.StringType),
    th.Property("title", th.StringType),
    th.Property("is_private", th.BooleanType),
    th.Property("application_ids", th.ArrayType(th.IntegerType)),
    th.Property(
        "phone_numbers",
        th.ArrayType(
            th.ObjectType(
                th.Property("value", th.StringType),
                th.Property("type", th.StringType),
            ),
        ),
    ),
    th.Property(
        "addresses",
        th.ArrayType(
            th.ObjectType(
                th.Property("value", th.StringType),
                th.Property("type", th.StringType),
            ),
        ),
    ),
    th.Property(
        "email_addresses",
        th.ArrayType(
            th.ObjectType(
                th.Property("value", th.StringType),
                th.Property("type", th.StringType),
            ),
        ),
    ),
    th.Property(
        "website_addresses",
        th.ArrayType(
            th.ObjectType(
                th.Property("value", th.StringType),
                th.Property("type", th.StringType),
            ),
        ),
    ),
    th.Property(
        "social_media_addresses",
        th.ArrayType(
            th.ObjectType(
                th.Property("value", th.StringType),
            ),
        ),
    ),
    th.Property(
        "recruiter",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("name", th.StringType),
            th.Property("employee_id", th.IntegerType),
        ),
    ),
    th.Property(
        "coordinator",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("name", th.StringType),
            th.Property("employee_id", th.IntegerType),
        ),
    ),
    th.Property("can_email", th.BooleanType),
    th.Property(
        "tags",
        th.ArrayType(th.StringType),
    ),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("last_activity", th.DateTimeType),
    th.Property("applications", application_schema),
)

schema_dict = schema.to_dict()

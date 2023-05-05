"""Activity Feeds schema."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property(
        "notes",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("created_at", th.StringType),
                th.Property("body", th.StringType),
                th.Property(
                    "user",
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("first_name", th.StringType),
                        th.Property("last_name", th.StringType),
                        th.Property("name", th.StringType),
                        th.Property("employee_id", th.StringType),
                    ),
                ),
                th.Property("private", th.BooleanType),
                th.Property("visibility", th.StringType),
            ),
        ),
    ),
    th.Property(
        "emails",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("created_at", th.StringType),
                th.Property("subject", th.StringType),
                th.Property("body", th.StringType),
                th.Property("to", th.StringType),
                th.Property("from", th.StringType),
                th.Property("cc", th.StringType),
                th.Property(
                    "user",
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("first_name", th.StringType),
                        th.Property("last_name", th.StringType),
                        th.Property("name", th.StringType),
                        th.Property("employee_id", th.StringType),
                    ),
                ),
            ),
        ),
    ),
    th.Property(
        "activities",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("created_at", th.StringType),
                th.Property("subject", th.StringType),
                th.Property("body", th.StringType),
                th.Property(
                    "user",
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("first_name", th.StringType),
                        th.Property("last_name", th.StringType),
                        th.Property("name", th.StringType),
                        th.Property("employee_id", th.StringType),
                    ),
                ),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()

"""Singer schema for Greenhouse Job Posts."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("title", th.StringType),
    th.Property(
        "location",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("office_id", th.NullableType(th.IntegerType)),
            th.Property(
                "job_post_location_type",
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                ),
            ),
        ),
    ),
    th.Property("internal", th.BooleanType),
    th.Property("external", th.BooleanType),
    th.Property("active", th.BooleanType),
    th.Property("live", th.BooleanType),
    th.Property("first_published_at", th.DateTimeType),
    th.Property("job_id", th.IntegerType),
    th.Property("content", th.StringType),
    th.Property("internal_content", th.StringType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("created_at", th.DateTimeType),
    th.Property("demographic_question_set_id", th.IntegerType),
    th.Property(
        "questions",
        th.ArrayType(
            th.ObjectType(
                th.Property("required", th.BooleanType),
                th.Property("private", th.BooleanType),
                th.Property("label", th.StringType),
                th.Property("name", th.StringType),
                th.Property("type", th.StringType),
                th.Property(
                    "values",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("value", th.IntegerType),
                            th.Property("label", th.StringType),
                        ),
                    ),
                ),
                th.Property("description", th.NullableType(th.StringType)),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()

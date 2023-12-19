"""JSON Schemas for Job Stages."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("job_id", th.IntegerType),
    th.Property("priority", th.IntegerType),
    th.Property(
        "interviews",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("schedulable", th.BooleanType),
                th.Property("estimated_minutes", th.IntegerType),
                th.Property(
                    "default_interviewer_users",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.IntegerType),
                            th.Property("first_name", th.StringType),
                            th.Property("last_name", th.StringType),
                            th.Property("name", th.StringType),
                            th.Property("employee_id", th.StringType),
                        ),
                    ),
                ),
                th.Property(
                    "interview_kit",
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("content", th.StringType),
                        th.Property(
                            "questions",
                            th.ArrayType(
                                th.ObjectType(
                                    th.Property("id", th.IntegerType),
                                    th.Property("question", th.StringType),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()

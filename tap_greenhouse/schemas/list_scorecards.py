"""Schema for List Scorecards."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("updated_at", th.StringType),
    th.Property("created_at", th.StringType),
    th.Property("interview", th.StringType),
    th.Property(
        "interview_step",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property("candidate_id", th.IntegerType),
    th.Property("application_id", th.IntegerType),
    th.Property("interviewed_at", th.StringType),
    th.Property(
        "submitted_by",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("name", th.StringType),
            th.Property("employee_id", th.StringType),
        ),
    ),
    th.Property(
        "interviewer",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("name", th.StringType),
            th.Property("employee_id", th.StringType),
        ),
    ),
    th.Property("submitted_at", th.StringType),
    th.Property("overall_recommendation", th.StringType),
    th.Property(
        "attributes",
        th.ArrayType(
            th.ObjectType(
                th.Property("name", th.StringType),
                th.Property("type", th.StringType),
                th.Property("note", th.StringType, nullable=True),
                th.Property("rating", th.StringType),
            ),
        ),
    ),
    th.Property(
        "ratings",
        th.ObjectType(
            th.Property("definitely_not", th.ArrayType(th.StringType)),
            th.Property("no", th.ArrayType(th.StringType)),
            th.Property("mixed", th.ArrayType(th.StringType)),
            th.Property("yes", th.ArrayType(th.StringType)),
            th.Property("strong_yes", th.ArrayType(th.StringType)),
        ),
    ),
    th.Property(
        "questions",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType, nullable=True),
                th.Property("question", th.StringType),
                th.Property("answer", th.StringType),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()

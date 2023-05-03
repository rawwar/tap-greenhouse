"""Applications Schema."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("candidate_id", th.IntegerType, required=True),
    th.Property("prospect", th.BooleanType),
    th.Property("applied_at", th.DateTimeType),
    th.Property("rejected_at", th.DateTimeType),
    th.Property("last_activity_at", th.DateTimeType),
    th.Property(
        "location",
        th.ObjectType(
            th.Property(
                "address",
                th.StringType,
            ),
        ),
    ),
    th.Property(
        "source",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("public_name", th.StringType),
        ),
    ),
    th.Property(
        "credited_to",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("name", th.StringType),
            th.Property("employee_id", th.StringType),
        ),
    ),
    th.Property("rejection_reason", th.StringType),
    th.Property("rejection_details", th.StringType),
    th.Property(
        "jobs",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
            ),
        ),
    ),
    th.Property("job_post_id", th.IntegerType),
    th.Property("status", th.StringType),
    th.Property(
        "current_stage",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "answers",
        th.ArrayType(
            th.ObjectType(
                th.Property("question", th.StringType),
                th.Property("answer", th.StringType),
            ),
        ),
    ),
    th.Property(
        "prospective_office",
        th.ObjectType(
            th.Property("primary_contact_user_id", th.StringType),
            th.Property("parent_id", th.StringType),
            th.Property("name", th.StringType),
            th.Property(
                "location",
                th.ObjectType(
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property("id", th.IntegerType),
            th.Property("external_id", th.StringType),
            th.Property("child_ids", th.ArrayType(th.StringType)),
        ),
    ),
    th.Property(
        "prospective_department",
        th.ObjectType(
            th.Property("parent_id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("id", th.IntegerType),
            th.Property("external_id", th.StringType),
            th.Property("child_ids", th.ArrayType(th.StringType)),
        ),
    ),
    th.Property(
        "prospect_detail",
        th.ObjectType(
            th.Property(
                "prospect_pool",
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "prospect_stage",
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "prospect_owner",
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                ),
            ),
        ),
    ),
    th.Property("custom_fields", th.ObjectType()),
    th.Property("keyed_custom_fields", th.ObjectType()),
    th.Property(
        "attachments",
        th.ArrayType(
            th.ObjectType(
                th.Property("filename", th.StringType),
                th.Property("url", th.StringType),
                th.Property("type", th.StringType),
                th.Property("created_at", th.DateTimeType),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()

"""Jobs Schema."""

from singer_sdk import typing as th

from tap_greenhouse.schemas.job_openings import schema as job_opening

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("name", th.StringType),
    th.Property("requisition_id", th.StringType),
    th.Property("notes", th.StringType),
    th.Property("confidential", th.BooleanType),
    th.Property("status", th.StringType),
    th.Property("created_at", th.DateTimeType),
    th.Property("opened_at", th.DateTimeType),
    th.Property("closed_at", th.DateTimeType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("is_template", th.BooleanType),
    th.Property("copied_from_id", th.IntegerType),
    th.Property(
        "departments",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("parent_id", th.IntegerType),
                th.Property("child_ids", th.ArrayType(th.IntegerType)),
                th.Property("external_id", th.StringType),
            ),
        ),
    ),
    th.Property(
        "offices",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property(
                    "location",
                    th.ObjectType(
                        th.Property("name", th.StringType),
                    ),
                ),
                th.Property("primary_contact_user_id", th.IntegerType),
                th.Property("parent_id", th.IntegerType),
                th.Property("child_ids", th.ArrayType(th.IntegerType)),
                th.Property("external_id", th.StringType),
            ),
        ),
    ),
    th.Property(
        "custom_fields",
        th.ObjectType(
            th.Property("region", th.StringType, required=False),
            th.Property("team", th.StringType, required=False),
            th.Property("employment_type", th.StringType, required=False),
            th.Property("credentials", th.StringType, required=False)
        ),
    ),
    th.Property("keyed_custom_fields", th.ObjectType()),
    th.Property(
        "hiring_team",
        th.ObjectType(
            th.Property(
                "hiring_managers",
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
                "recruiters",
                th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("first_name", th.StringType),
                        th.Property("last_name", th.StringType),
                        th.Property("name", th.StringType),
                        th.Property("employee_id", th.StringType),
                        th.Property("responsible", th.BooleanType),
                    ),
                ),
            ),
            th.Property(
                "coordinators",
                th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("first_name", th.StringType),
                        th.Property("last_name", th.StringType),
                        th.Property("name", th.StringType),
                        th.Property("employee_id", th.StringType),
                        th.Property("responsible", th.BooleanType),
                    ),
                ),
            ),
            th.Property(
                "sourcers",
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
        ),
    ),
    th.Property("openings", th.ArrayType(job_opening)),  # use job opening schema here
)

schema_dict = schema.to_dict()

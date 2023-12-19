"""Schema for users stream."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("first_name", th.StringType),
    th.Property("last_name", th.StringType),
    th.Property("primary_email_address", th.StringType),
    th.Property("updated_at", th.DateTimeType),
    th.Property("created_at", th.DateTimeType),
    th.Property("disabled", th.BooleanType),
    th.Property("site_admin", th.BooleanType),
    th.Property("emails", th.ArrayType(th.StringType)),
    th.Property("employee_id", th.StringType),
    th.Property("linked_candidate_ids", th.ArrayType(th.IntegerType)),
    th.Property(
        "offices",
        th.ArrayType(
            th.PropertiesList(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property(
                    "location",
                    th.PropertiesList(th.Property("name", th.StringType)),
                ),
                th.Property("primary_contact_user_id", th.IntegerType),
                th.Property("parent_id", th.IntegerType),
                th.Property("parent_office_external_id", th.StringType),
                th.Property("child_ids", th.ArrayType(th.IntegerType)),
                th.Property("child_office_external_ids", th.ArrayType(th.StringType)),
                th.Property("external_id", th.StringType),
            ),
        ),
    ),
    th.Property(
        "departments",
        th.ArrayType(
            th.PropertiesList(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("parent_id", th.IntegerType),
                th.Property("parent_department_external_id", th.StringType),
                th.Property("child_ids", th.ArrayType(th.IntegerType)),
                th.Property(
                    "child_department_external_ids",
                    th.ArrayType(th.StringType),
                ),
                th.Property("external_id", th.StringType),
            ),
        ),
    ),
)


schema_dict = schema.to_dict()

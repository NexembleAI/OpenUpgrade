from openupgradelib import openupgrade


def _rename_tables(env):
    # we delete sql constraint before table rename
    openupgrade.delete_sql_constraint_safely(
        env,
        "hr_employee",
        "employee_work_location",
        "hr_employee_work_location_id_fkey",
    )
    openupgrade.rename_tables(
        env.cr, [("employee_work_location", "hr_work_location")]
    )


def _rename_fields(env):
    openupgrade.rename_fields(
        env,
        [
            (
                "hr.work.location",
                "hr_work_location",
                "personal_email",
                "private_email",
            ),
        ],
    )


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.convert_field_to_html(
        env.cr, "hr_employee", "departure_description", "departure_description"
    )
    openupgrade.convert_field_to_html(env.cr, "hr_job", "description", "description")
    _rename_tables(env)
    _rename_fields(env)
    


from wtforms.validators import ValidationError
from sqladmin import ModelView
from attendance.models.ip_model import IP
from internals.utils.check_ip_valid import is_valid_ip


def validate_ip(form, field):
    if not is_valid_ip(form.ip_address.data):
        raise ValidationError(f"IP not valid: {form.ip_address.data}")


class IPAdmin(ModelView, model=IP):
    name = "IP"
    page_size_options = [25, 50, 100, 200]
    category = "Meeting MPC"

    can_create = True
    can_delete = True

    column_list = [
        IP.id,
        IP.ip_address,
        IP.description
    ]

    form_excluded_columns = [IP.meetings]

    form_args = {
        "ip_address": {
            "validators": [validate_ip]
        },
    }

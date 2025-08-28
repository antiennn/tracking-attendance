from wtforms.validators import ValidationError
from sqladmin import ModelView
from attendance.models.ip_model import IP
from internals.utils.check_ip_valid import is_valid_ip


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

    async def on_model_change(self, data, model, is_created, request):
        ip_value = data.get("ip_address")
        if not is_valid_ip(ip_value):
            raise ValidationError(f"IP not valid: {ip_value}")

        return await super().on_model_change(data, model, is_created, request)

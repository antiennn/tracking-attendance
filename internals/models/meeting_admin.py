from markupsafe import Markup
from sqladmin import ModelView
from slugify import slugify
from sqladmin.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired, ValidationError

from attendance.models.meeting_model import Meeting


def validate_time_range(form, field):
    if form.start_at.data and form.end_at.data:
        if form.start_at.data >= form.end_at.data:
            raise ValidationError("Thời gian kết thúc phải lớn hơn thời gian bắt đầu")


class MeetingAdmin(ModelView, model=Meeting):
    name = "Meeting"
    page_size_options = [25, 50, 100, 200]
    category = "Meeting MPC"
    list_template = "sqladmin/list_override.html"

    can_create = True
    can_delete = True

    column_list = [
        Meeting.id,
        Meeting.name,
        "View link",
        "QR download",
        "Copy to clipboard",
        "Detail"
    ]

    form_excluded_columns = [
        Meeting.attendances,
        Meeting.created_at,
        Meeting.updated_at,
    ]


    form_overrides = {
        "ips": QuerySelectMultipleField
    }

    form_args = {
        "ips": {
            "label": "Find IP",
            "validators": [DataRequired()],
            "allow_blank": True,
        },
        "start_at": {
            "validators": [DataRequired(message="Start time is required")],
        },
        "end_at": {
            "validators": [DataRequired(message="End time is required"), validate_time_range],
        },
    }

    column_formatters = {
        "View link": lambda m, a: Markup(f'<a href="/attendance/meetings/{m.id}" target="_blank" '
                                         f'style="text-decoration: none">🔗</a>'),
        "QR download": lambda m, _: Markup(f'<a href="/api/attendance/meetings/{m.id}/qr" target="_blank" '
                                           f'style="text-decoration:none">📥</a>'),
        "Copy to clipboard": lambda m, a: Markup(
            f'<button onclick="copyToClipboard(\'/attendance/meetings/{m.id}\')" '
            f'style="border:none; background:none; cursor:pointer">📋</button>'
        ),
        "Detail": lambda m, _: Markup(f'<a href="/admin/attendance/list?meeting_id={m.id}" '
                                      f'style="text-decoration:none">Detail</a>'),
    }

    async def on_model_change(self, data, model, is_created, request):
        if is_created or "name" in data:
            model.id = slugify(data["name"])
        return model

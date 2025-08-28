from sqladmin import ModelView
from slugify import slugify
from sqladmin.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired

from attendance.models.meeting_model import Meeting


class MeetingAdmin(ModelView, model=Meeting):
    name = "Meeting"
    page_size_options = [25, 50, 100, 200]
    category = "Meeting MPC"

    can_create = True
    can_delete = True

    column_list = [
        Meeting.id,
        Meeting.name,
    ]

    form_excluded_columns = [
        Meeting.attendances,
        Meeting.created_at,
        Meeting.updated_at,
    ]

    extra_css = [
        "https://cdn.jsdelivr.net/npm/choices.js/public/assets/styles/choices.min.css"
    ]

    extra_js = [
        "https://cdn.jsdelivr.net/npm/choices.js/public/assets/scripts/choices.min.js",
        "/static/js/select-many-to-many.js",
    ]

    form_overrides = {
        "ips": QuerySelectMultipleField
    }

    form_args = {
        "ips": {
            "label": "Find IP",
            "validators": [DataRequired()],
            "allow_blank": True,
        }
    }

    async def on_model_change(self, data, model, is_created, request):
        if is_created or "name" in data:
            model.id = slugify(data["name"])
        return model

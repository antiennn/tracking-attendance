from sqladmin import ModelView
from sqladmin.filters import AllUniqueStringValuesFilter

from attendance.models.attendance_model import Attendance


class AttendanceAdmin(ModelView, model=Attendance):
    name = "Attendance"
    page_size_options = [25, 50, 100, 200]
    category = "Meeting MPC"

    can_create = False
    can_delete = False

    column_searchable_list = [
        Attendance.name
    ]

    column_filters = [
        AllUniqueStringValuesFilter(Attendance.meeting_id),
    ]

    column_list = [
        Attendance.name,
        Attendance.attended_at,
        Attendance.device_id
    ]

from fastapi import FastAPI
from sqladmin import Admin

from attendance.apis import attendance_api
from common.apis import utils_api

from attendance.views import attendance_view

from config import settings
from database import engine
from internals.admin import AdminAuth
from internals.models.ip_admin import IPAdmin
from internals.models.meeting_admin import MeetingAdmin

app = FastAPI()
authentication_backend = AdminAuth(secret_key=settings.ADMIN_SECRET_KEY)
admin = Admin(app, engine, base_url="/admin",
              authentication_backend=authentication_backend,
              title="Tracking Attendance MPC")

admin.add_view(MeetingAdmin)
admin.add_view(IPAdmin)

app.include_router(prefix="/api", router=attendance_api.router, dependencies=[])
app.include_router(prefix="/api", router=utils_api.router, dependencies=[])

app.include_router(prefix="/attendance", router=attendance_view.router, dependencies=[])

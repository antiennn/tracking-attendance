from fastapi import FastAPI
from jinja2 import ChoiceLoader, FileSystemLoader
from sqladmin import Admin
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.staticfiles import StaticFiles

from attendance.apis import attendance_api
from common.apis import utils_api

from attendance.views import attendance_view

from config import settings
from database import engine
from internals.admin import AdminAuth
from internals.models.ip_admin import IPAdmin
from internals.models.meeting_admin import MeetingAdmin
from internals.models.attendance_admin import AttendanceAdmin
from common import get_csrf_config

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOST
)

app.mount("/static", StaticFiles(directory="internals/static"), name="static")


authentication_backend = AdminAuth(secret_key=settings.ADMIN_SECRET_KEY)
admin = Admin(app, engine, base_url="/admin",
              authentication_backend=authentication_backend,
              templates_dir="internals/static/templates",
              title="Tracking Attendance MPC")

admin.add_view(MeetingAdmin)
admin.add_view(IPAdmin)
admin.add_view(AttendanceAdmin)

app.include_router(prefix="/api", router=attendance_api.router, dependencies=[])
app.include_router(prefix="/api", router=utils_api.router, dependencies=[])

app.include_router(prefix="/attendance", router=attendance_view.router, dependencies=[])

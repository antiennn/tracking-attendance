from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="", tags=["Attendance"])
templates = Jinja2Templates(directory="attendance/templates")


@router.get("/meetings/{meeting_id}", response_class=HTMLResponse)
async def meeting_page(request: Request, meeting_id: str):
    return templates.TemplateResponse("attendance.html", {"request": request, "meeting_id": meeting_id})

from fastapi import APIRouter, Request, Depends, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_csrf_protect import CsrfProtect

router = APIRouter(prefix="", tags=["Attendance"])
templates = Jinja2Templates(directory="attendance/templates")


@router.get("/meetings/{meeting_id}", response_class=HTMLResponse)
async def meeting_page(request: Request, response: Response, meeting_id: str, csrf_protect: CsrfProtect = Depends()):
    csrf_access_token, csrf_cookie = csrf_protect.generate_csrf_tokens()

    response = templates.TemplateResponse(
        "attendance.html",
        {"request": request, "meeting_id": meeting_id, "csrf_token": csrf_access_token}
    )
    response.set_cookie(
        key="fastapi-csrf-token",
        value=csrf_cookie,
        httponly=True
    )
    return response

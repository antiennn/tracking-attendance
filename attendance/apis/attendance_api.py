from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi_csrf_protect import CsrfProtect
from sqlalchemy.orm import Session
from sqlalchemy import select, exists, and_, case
from starlette import status

from attendance.models.attendance_model import Attendance
from attendance.models.meeting_model import Meeting
from attendance.schemas.attendance_schema import AttendanceSchema
from attendance.utils.get_client_ip import get_client_ip
from database import get_db

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post("/meetings/{meeting_id}", status_code=status.HTTP_201_CREATED)
async def attend_meeting(meeting_id: str, request: Request, payload: AttendanceSchema, db: Session = Depends(get_db),
                         csrf_protect: CsrfProtect = Depends()):

    try:
        await csrf_protect.validate_csrf(request)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))

    client_ip = get_client_ip(request)

    meeting = db.query(Meeting).filter_by(id=meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    if not meeting.ips:
        raise HTTPException(status_code=403, detail="No IPs allowed for this meeting")

    allowed_ips = [current_ip.ip_address for current_ip in meeting.ips]
    if client_ip not in allowed_ips:
        raise HTTPException(status_code=403, detail=f"IP {client_ip} not allowed")

    stmt = select(
        case(
            (
                exists().where(
                    and_(Attendance.meeting_id == meeting_id,
                         Attendance.name == payload.name)
                ),
                "attended"
            ),
            (
                exists().where(
                    and_(Attendance.meeting_id == meeting_id,
                         Attendance.device_id == payload.device_id)
                ),
                "fraud"
            ),
            else_="ok"
        )
    )

    result = db.execute(stmt).scalar()

    if result == "attended":
        raise HTTPException(status_code=400, detail="Already attended")
    elif result == "fraud":
        raise HTTPException(status_code=400, detail="fraud detected")

    new_attendance = Attendance(
        meeting_id=meeting_id,
        name=payload.name,
        ip_address=client_ip,
        device_id=payload.device_id,
    )
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return {
        "status": "success",
        "meeting_id": meeting_id,
        "user_id": payload.name,
        "ip": client_ip,
    }

from sqlalchemy import Column, String, text, TIMESTAMP
from sqlalchemy.orm import relationship
from attendance.models.attendance_model import Attendance
from attendance.models.ip_meeting_model import MeetingIP
from database import Base


class Meeting(Base):
    __tablename__ = "meeting"
    id = Column(String, primary_key=True, unique=True, index=True)
    name = Column(String)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )
    start_at = Column(
        TIMESTAMP(timezone=True), nullable=True
    )
    end_at = Column(
        TIMESTAMP(timezone=True), nullable=True
    )
    attendances = relationship("Attendance", back_populates="meeting")

    ips = relationship(
        "IP",
        secondary="meeting_ip",
        back_populates="meetings"
    )

    def __str__(self):
        return self.name

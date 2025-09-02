from sqlalchemy import Column, String, text, TIMESTAMP, Boolean, event
from sqlalchemy.orm import relationship
from datetime import datetime, timezone, timedelta
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
        TIMESTAMP(timezone=True), nullable=True, onupdate=text("now()")
    )
    start_at = Column(
        TIMESTAMP(timezone=False), nullable=True
    )
    end_at = Column(
        TIMESTAMP(timezone=False), nullable=True
    )
    attendances = relationship("Attendance", back_populates="meeting", cascade="all, delete")

    is_active = Column(Boolean, default=True)

    ips = relationship(
        "IP",
        secondary="meeting_ip",
        back_populates="meetings"
    )

    def check_active(self):
        now = (datetime.now(timezone.utc) + timedelta(hours=7)).replace(tzinfo=None)

        self.is_active = self.start_at <= now <= self.end_at

    def __str__(self):
        return self.name


@event.listens_for(Meeting, 'load')
def pre_load_data(target, context):
    target.check_active()

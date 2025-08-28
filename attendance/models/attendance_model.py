from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    meeting_id = Column(String, ForeignKey("meeting.id"))
    ip_address = Column(String(100), nullable=False)
    device_id = Column(String(255), nullable=False)

    meeting = relationship("Meeting", back_populates="attendances")

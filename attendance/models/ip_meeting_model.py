from sqlalchemy import ForeignKey, Column, Integer, String
from database import Base


class MeetingIP(Base):
    __tablename__ = "meeting_ip"

    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(String, ForeignKey("meeting.id", ondelete="CASCADE"))
    ip_id = Column(Integer, ForeignKey("ip.id", ondelete="CASCADE"))

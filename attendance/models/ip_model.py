from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class IP(Base):
    __tablename__ = "ip"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String(45), unique=True, nullable=False)
    description = Column(String, nullable=False)

    meetings = relationship(
        "Meeting",
        secondary="meeting_ip",
        back_populates="ips"
    )

    def __str__(self):
        return self.description

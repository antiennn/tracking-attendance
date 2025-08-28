from typing import Optional

from pydantic import BaseModel


class AttendanceSchema(BaseModel):
    name: Optional[str]
    device_id: Optional[str]

    class Config:
        from_attributes = True

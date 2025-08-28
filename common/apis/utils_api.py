from fastapi import APIRouter, Request
from starlette import status


from attendance.utils.get_client_ip import get_client_ip

router = APIRouter(prefix="", tags=["Common"])


@router.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": "pong"}


@router.get("/current-ip", status_code=status.HTTP_200_OK)
async def read_root(request: Request):
    client_ip = get_client_ip(request)
    return {"message": client_ip}

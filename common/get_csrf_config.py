from fastapi_csrf_protect import CsrfProtect
from pydantic import BaseModel

from config import settings


class CsrfSettings(BaseModel):
    secret_key: str = settings.CSRF_COOKIES


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings(secret_key=settings.CSRF_COOKIES)

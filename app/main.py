from fastapi.openapi.models import Response
from starlette import status

from app.api.base import init_fast_api
from app.api.settings import settings
from app.api.v1.api import api_router
from app.dto.health_state import HealthState


async def health_check_handler(response: Response) -> HealthState:
    response.status_code = status.HTTP_200_OK
    return HealthState(state="OK")


app = init_fast_api(settings, api_router, lambda: HealthState(state="OK"))


@app.on_event("startup")
def on_startup():
    pass

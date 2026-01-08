import uvicorn
from fastapi import FastAPI
from booking_service.src.api.endpoints import router
from booking_service.src.singleton.impls.configuration import Configuration


def init_service():
    config = Configuration().settings
    app = FastAPI()
    app.include_router(router=router)
    uvicorn.run(app, host=config.server_api.host, port=config.server_api.port)

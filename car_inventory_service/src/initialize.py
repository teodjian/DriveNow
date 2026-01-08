import uvicorn
from fastapi import FastAPI
from car_inventory_service.src.api.endpoints import router
from car_inventory_service.src.singleton.impls.configuration import Configuration


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=router)
    return app


def init_service():
    config = Configuration().settings
    app = create_app()
    uvicorn.run(app, host=config.server_api.host, port=config.server_api.port)

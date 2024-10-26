from fastapi import APIRouter
from src.interfaces.api.controllers import hello_world_controller

def hello_world_routes(router: APIRouter):
    router.include_router(hello_world_controller.router, prefix="/api")
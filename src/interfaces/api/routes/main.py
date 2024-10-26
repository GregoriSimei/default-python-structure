from fastapi import APIRouter
from src.interfaces.api.routes.hello_world_routes import hello_world_routes

router = APIRouter()
hello_world_routes(router)

from fastapi import FastAPI
from src.interfaces.api.routes.main import router

app = FastAPI()
app.include_router(router)
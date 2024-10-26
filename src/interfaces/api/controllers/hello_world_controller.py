from fastapi import Depends, APIRouter
from src.application.use_cases.hello_world_use_case import HelloWorldUseCase

router = APIRouter()

def get_hello_world_use_case():
    return HelloWorldUseCase()

@router.get("/hello")
def hello_world_controller(use_case: HelloWorldUseCase = Depends(get_hello_world_use_case)):
    return use_case.execute()
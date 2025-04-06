from fastapi import APIRouter
from routes.log.login import login
from routes.signup.register import register

api_router = APIRouter()

api_router.include_router(register.router, prefix="", tags=["users-router"])
api_router.include_router(login.router, prefix="", tags=["auth-router"])
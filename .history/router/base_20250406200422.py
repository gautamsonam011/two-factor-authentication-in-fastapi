from fastapi import APIRouter
from router.log.login import login
from router.signup.register import register

api_router = APIRouter()
api_router.include_router(register.router, prefix="", tags=["users-router"])
api_router.include_router(login.router, prefix="", tags=["auth-router"])
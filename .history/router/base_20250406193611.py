from fastapi import APIRouter
from router.login.login import route_login
from router.register import route_signup

api_router = APIRouter()
api_router.include_router(route_signup.router, prefix="", tags=["users-webapp"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapp"])
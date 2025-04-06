# routes/base.py
from fastapi import APIRouter
from routes.log.login import router as login_router  
from routes.signup.register import router as register_router 

api_router = APIRouter()

api_router.include_router(register_router, prefix="/signup", tags=["users-router"])
api_router.include_router(login_router, prefix="/auth", tags=["auth-router"])

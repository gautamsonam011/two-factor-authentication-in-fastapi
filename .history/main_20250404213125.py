from core.config import settings
from database.base import Base
from database.seession import egine
from database.utils import check_db_connected
from database.utils import check_db_disconnected
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from webapps.base import api_router as web_app_router


def include_router(app):
    app.include_router
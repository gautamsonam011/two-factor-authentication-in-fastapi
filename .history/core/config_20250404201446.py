import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".")/".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Two-Factor-Authentication"
    PROJECT_VERSION: str = "1.0.0"

     # To configure database
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5433
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()    
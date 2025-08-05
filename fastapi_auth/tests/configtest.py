import os
import sys
from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
from app.config.database import Base, get_session
from app.models import User

USER_NAME = "ONLYPURITY"
USER_EMAIL = "Udeheberepurity@gmail.com"
FIRST_NAME = "Purity" 
USER_PASSWORD = "password@123"

engine = create_engine("sqlite:///./fastapi.db")
SessionTesting = sessionmaker(autocomit=False, autoflush=False, bind=engine)


# from functools import lru_cache
# from pydantic_settings import BaseSettings 
# from pathlib import Path
# from dotenv import load_dotenv
# from urllib.parse import quote_plus

# env_path = Path(".") / ".env"
# load_dotenv(dotenv_path=env_path)


# class Settings(BaseSettings):
    
    
#     APP_NAME: str = os.environ.get("APP_NAME", "FastAPI")
#     DEBUG: bool = bool(os.environ.get("DEBUG", False))
    
    
@pytest.fixture(scope="function")
def app_test() -> Generator:
     session = SessionTesting()
     try:
         yield session
     finally:
         session.close()


@pytest.fixture(scope ="function")
def app_test():
    Base.metadata.create_all(bind=engine)
    yield app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(app_test, test_session):
    def _test_db():
        try:
           yield test_session
        finally:
         pass 

    app.dependency_overrides[get_session] = _test_db
    with TestClient(app_test) as client:
        response = client.get("/")
    assert response.status_code == 200
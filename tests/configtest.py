import os
from functools import lru_cache
from pydantic_settings import BaseSettings 
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    
    
    APP_NAME: str = os.environ.get("APP_NAME", "FastAPI")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))



    
    
    
    
 @pytest.fixture(scope="function")
 def app_test() -> Generator:
     session = SessionTesting()
     try:
         yield session
     finally:
         session.close()


@pytest.fixture(scope ="function")
def app_test();
    Base.metaata.create_all(bind=engine)
    yield app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(app_test, test_session):
    def _test_db():
      try:
        yield test_session
        finally
        pass 

app.test.dependency_overrides[get_session] = _test_db
return TestClient(app_test)
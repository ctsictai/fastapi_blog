from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql+pymysql://mysql:mysql@localhost")
Session = sessionmaker(bind=engine)
class Settings(BaseSettings):
    openapi_url:str = "/openapi.json"
    
    
    
settings = Settings()
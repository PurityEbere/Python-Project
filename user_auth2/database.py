from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessioonmaker


SQLALCHEMY_DATABASE_URL = "sqite:///./sql_app.db"

engine =create_engine(SQLALCHEMY_DATABASE_URL)
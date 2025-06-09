from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


user = "hr"
passwd = "hr"
host = "127.0.0.1"
port = "3306"
db = "mysql"

DB_URL = f'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}'

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base = declarative_base()

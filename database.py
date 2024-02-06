from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Base
from config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print('creating Base') 
Base = declarative_base()


def init_db():

    Base.metadata.create_all(bind=engine)

    SessionLocal.add(
        Base(username="testuser", password_hash=b"", password_salt=b"", balance=1)
    )
    SessionLocal.commit()

    print("Initialized the db")


if __name__ == "__main__":
    init_db()
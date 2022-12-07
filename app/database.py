from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

                         #"postgresql://<username>:<password>@<ip-adress/hostname>/<database_name>"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@localhost/freefinance"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

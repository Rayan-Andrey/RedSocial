from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#comentarta cual base es la que se esta usando

DATABASE_URL = "mysql+pymysql://root:password@localhost/red_social"
#DATABASE_URL = "mysql+pymysql://root:Admin@localhost/red_social"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False , bind=engine)

Base = declarative_base()
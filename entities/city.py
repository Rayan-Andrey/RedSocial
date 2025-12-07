from sqlalchemy import Column, Integer,String
from persistence.db import Base,SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class City(Base):
    __tablename__="city"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60),nullable=False)

    def save(self):
        session = SessionLocal()
        try:
            session.add(self)
            session.commit()
            session.refresh(self)
            return self.id
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()

    def update(self, name):
        session = SessionLocal()
        try:
            city = session.query(City).filter_by(id = self.id).first()
            if city: 
                city.name = name
                session.commit()
                session.refresh(city)
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
             session.close()

    def delete(self):
        session = SessionLocal()
        try:
            city = session.query(City).filter_by(id = self.id).first()
            if city: 
                session.delete(city)
                session.commit()
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()

def get_all():
    session = SessionLocal()
    try:
        return session.query(City).all()
    finally:
        session.close()
    
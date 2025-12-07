from sqlalchemy import Column, Integer,String
from persistence.db import Base,SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class Costumer(Base):
    __tablename__="costumer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    costumer_name     = Column(String(60),nullable=False)
    costumer_phone    = Column(String(15),nullable=False)
    costumer_email    = Column(String(60),nullable=False)
    costumer_zip_code = Column(String(10),nullable=False)

    def save(self):
        session = SessionLocal()
        try:
            session.add(self)
            session.commit()
            session.refresh(self)
            return self.id
        finally:
            session.close()

    def update(self, name, phone, email,zip):
        session = SessionLocal()
        try:
            costumer = session.query(Costumer).filter_by(id = self.id).first()
            if costumer: 
                costumer.costumer_name  = name
                costumer.costumer_phone  = phone
                costumer.costumer_email  = email
                costumer.costumer_zip_code  = zip
                session.commit()
                session.refresh(costumer)
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
             session.close()

    def delete(self):
        session = SessionLocal()
        try:
            costumer = session.query(Costumer).filter_by(id = self.id).first()
            if costumer: 
                session.delete(costumer)
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
        return session.query(Costumer).all()
    finally:
        session.close()
    
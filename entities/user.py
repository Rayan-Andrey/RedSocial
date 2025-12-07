from sqlalchemy import Column,Integer,String, DATETIME
from persistence.db import Base,SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class User(Base):
    __tablename__="usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50),nullable=False)
    correo = Column(String(100),nullable=False, unique=True)
    edad = Column(Integer)
    foto_perfil = Column(String(255),default="/static/images/usuarios/default.png")
    fecha_registro =Column(DATETIME ,default= datetime.utcnow)

    def save_user(self):
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

    def update_user(self,nombre, correo, edad, foto_perfil):
        session = SessionLocal()
        try:
            user = session.query(User).filter_by(id = self.id).first()
            if user: 
                user.nombre = nombre
                user.correo = correo
                user.edad = edad
                user.foto_perfil = foto_perfil
                session.commit()
                session.refresh(user)
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
             session.close()

    def delete_user(self):
        session = SessionLocal()
        try:
            user = session.query(User).filter_by(id = self.id).first()
            if user: 
                session.delete(user)
                session.commit()
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()
    
    @staticmethod
    def get_all_user():
        session = SessionLocal()
        try:
            return session.query(User).all()
        finally:
            session.close()
    
from sqlalchemy import Column,Integer,String,Text, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from persistence.db import Base,SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class Coment(Base):
    __tablename__="comentarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contenido = Column(Text, nullable = False)
    fecha = Column(DATETIME ,default= datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    hilo_id = Column(Integer, ForeignKey('hilos.id'), nullable=False)

    usuarios = relationship("User", back_populates="comentarios")
    hilos = relationship("Thread", back_populates="comentarios")
    likes = relationship("Like", back_populates="comentarios")

    def save_coment(self):
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

    def update_coment(self,conment):
        session = SessionLocal()
        try:
            coment = session.query(Coment).filter_by(id = self.id).first()
            if coment: 
                coment.coment = coment
                session.commit()
                session.refresh(coment)
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
             session.close()

    def delete_coment(self):
        session = SessionLocal()
        try:
            coment = session.query(Coment).filter_by(id = self.id).first()
            if coment: 
                session.delete(coment)
                session.commit()
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()
    
    @staticmethod
    def get_all_coment():
        session = SessionLocal()
        try:
            return session.query(Coment).all()
        finally:
            session.close()
    
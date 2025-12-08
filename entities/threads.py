from sqlalchemy import Column,Integer,String,Text, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from persistence.db import Base,SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class Thread(Base):
    __tablename__ = "hilos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(50))
    imagen = Column(String(255))
    contenido = Column(Text)
    titulo = Column(String(100), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    fecha = Column(DATETIME, default=datetime.utcnow)

    usuarios = relationship("User", back_populates="hilos")
    likes = relationship("Like", back_populates="hilos")
    comentarios = relationship("Coment", back_populates="hilos")

    def save_thread(self):
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

    def update_thread(self,categoria, imagen, contenido, titulo):
        session = SessionLocal()
        try:
            thread = session.query(Thread).filter_by(id = self.id).first()
            if thread: 
                thread.categoria = categoria
                thread.imagen = imagen
                thread.contenido = contenido
                thread.titulo = titulo
                session.commit()
                session.refresh(thread)
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
             session.close()

    def delete_thread(self):
        session = SessionLocal()
        try:
            thread = session.query(Thread).filter_by(id = self.id).first()
            if thread: 
                session.delete(thread)
                session.commit()
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()
    
    @staticmethod
    def get_all_thread():
        session = SessionLocal()
        try:
            return session.query(Thread).all()
        finally:
            session.close()
    
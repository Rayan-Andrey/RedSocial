from sqlalchemy import Column,Integer, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from persistence.db import Base,SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    hilo_id = Column(Integer, ForeignKey('hilos.id'))
    comentario_id = Column(Integer, ForeignKey('comentarios.id'))
    fecha = Column(DATETIME, default=datetime.utcnow)

    # Relationships
    usuarios = relationship("User", back_populates="likes")
    hilos = relationship("Thread", back_populates="likes")
    comentarios = relationship("Coment", back_populates="likes")

    def save_like(self):
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

    def update_like(self,categoria, imagen, contenido, titulo):
        session = SessionLocal()
        try:
            like = session.query(Like).filter_by(id = self.id).first()
            if like: 
                like.categoria = categoria
                like.imagen = imagen
                like.contenido = contenido
                like.titulo = titulo
                session.commit()
                session.refresh(like)
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
             session.close()

    def delete_like(self):
        session = SessionLocal()
        try:
            like = session.query(Like).filter_by(id = self.id).first()
            if like: 
                session.delete(like)
                session.commit()
                return True
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()
    
    @staticmethod
    def get_all_like():
        session = SessionLocal()
        try:
            return session.query(Like).all()
        finally:
            session.close()
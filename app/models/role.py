from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    descripcion = Column(String, nullable=True)  # 👈 nuevo campo

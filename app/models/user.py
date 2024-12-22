from sqlalchemy import Column, Integer, String

from app.db.session import Base


# Modelo SQLAlchemy para la base de datos
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=True)  # Campo opcional para v2

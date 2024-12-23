import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base
from app.models.user import User 


# Configuración para usar SQLite para las pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas para las pruebas
@pytest.fixture(scope="module")
def test_db():
    # Crear todas las tablas necesarias para las pruebas
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db  # Pasamos la sesión a las pruebas
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)  # Limpiar las tablas después de las pruebas

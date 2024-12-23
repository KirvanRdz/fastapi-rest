import pytest
from fastapi import HTTPException
from app.services.user_service import check_user_exists, create_user, authenticate_user
from app.models.user import User
from app.schemas.auth import Login


# Prueba para verificar que un usuario ya existe
def test_check_user_exists(test_db):
    user_data = { "name": "New User", "email": "new@example.com", "password": "password123" }
    
    # Crear un usuario en la base de datos
    create_user(test_db, **user_data)
    
    # Verificar que el usuario ya existe
    with pytest.raises(HTTPException):
        check_user_exists(test_db, user_data["email"])

# Prueba para crear un usuario
def test_create_user(test_db):
    
    user_data = { "name": "New User", "email": "new2@example.com", "password": "password123" }
    user = create_user(test_db, **user_data)
    
    # Verificar que el usuario se ha creado correctamente
    assert user.name == user_data["name"]
    assert user.email == user_data["email"]
    assert user.password != user_data["password"]  # El password debe estar hasheado

# Prueba para autenticar un usuario con credenciales correctas
def test_authenticate_user_correct(test_db):
    user_data = { "name": "New User", "email": "new3@example.com", "password": "password123" }
    create_user(test_db, **user_data)
    login_data = Login(email=user_data["email"], password=user_data["password"])
    
    user = authenticate_user(test_db, login_data)
    
    assert user is not None
    assert user.email == user_data["email"]

# Prueba para autenticar un usuario con credenciales incorrectas
def test_authenticate_user_incorrect(test_db):
    user_data = { "name": "New User", "email": "new4@example.com", "password": "password123" }
    create_user(test_db, **user_data)
    login_data = Login(email=user_data["email"], password="wrongpassword")
    
    user = authenticate_user(test_db, login_data)
    
    assert user is None

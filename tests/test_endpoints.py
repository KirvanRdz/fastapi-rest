import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.user import User

client = TestClient(app)

# Variable global para almacenar token
access_token_global = None
refresh_token_global = None

@pytest.fixture(scope="module")
def test_db(test_db):
    return test_db


def test_register_user(test_db):
    # Datos de entrada
    user_data = {
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "testpassword123"
    }

    # Realizar la petición POST al endpoint /register
    response = client.post("/api/v1/auth/register", json=user_data)

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 201
    assert response.json()["email"] == user_data["email"]

    # Verificar que el usuario se haya creado en la base de datos
    db_user = test_db.query(User).filter(User.email == user_data["email"]).first()
    assert db_user is not None
    assert db_user.name == user_data["name"]

def test_login_user():
    
    # Usamos la variable global
    global access_token_global  
    global refresh_token_global

    # Datos de entrada para el login
    user_data = {
        "email": "testuser@example.com",
        "password": "testpassword123"
    }

    # Realizar la petición POST al endpoint /login
    response = client.post("/api/v1/auth/login", json=user_data)

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200
    assert "access_token" in response.cookies
    assert "refresh_token" in response.cookies

    # Guardar los token en la variable global
    access_token_global = response.cookies["access_token"]
    refresh_token_global = response.cookies["refresh_token"]


def test_verify_token():
    global access_token_global  # Accedemos a la variable global

    # Verificar que el access_token global esté disponible
    assert access_token_global is not None

    # Realizar la petición GET al endpoint /verify_token
    response = client.get("/api/v1/auth/verify_token", cookies={"access_token": access_token_global})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200
    assert response.json()["message"] == "Acces token valido"

def test_refresh_token(test_db):
    # Accedemos a la variable global
    global refresh_token_global  
    global access_token_global  

    # Realizar la petición POST al endpoint /refresh_token
    response = client.post("/api/v1/auth/refresh_token", cookies={"refresh_token": refresh_token_global})

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200
    assert "access_token" in response.cookies
    assert response.json()["message"] == "Access token renovado exitosamente"

def test_logout(test_db):
    # Realizar la petición POST al endpoint /logout
    response = client.post("/api/v1/auth/logout")

    # Verificar que la respuesta sea exitosa
    assert response.status_code == 200
    assert response.json()["message"] == "Cerró sesión exitosamente"
    assert "access_token" not in response.cookies
    assert "refresh_token" not in response.cookies

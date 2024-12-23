from fastapi import APIRouter, Depends, Response, status

from app.db.session import get_db
from app.core.versionado import versioned
from app.core.auth import create_access_token, create_refresh_token, set_cookies
from app.schemas.user import UserV1, UserResponseV1
from app.schemas.auth import Login
from app.services.user_service import check_user_exists, create_user, authenticate_user
from app.utils.error_handling import raise_unauthorized_error

router = APIRouter()

@versioned(version="v1")
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponseV1)
def register_user(user_data: UserV1, db=Depends(get_db)):
    
    # Verificar si el usuario ya existe
    check_user_exists(db, user_data.email)
    
    # Crear el usuario
    db_user = create_user(db, user_data.name, user_data.email, user_data.password)
    
    return db_user

@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserResponseV1 )
def login_user(user: Login, response: Response, db=Depends(get_db)):
    
    authenticated_user = authenticate_user(db, user)
    
    if not authenticated_user:
        raise_unauthorized_error("Credenciales inválidas")
    
    # Generar los tokens
    access_token = create_access_token(data={"sub": authenticated_user.email})
    refresh_token = create_refresh_token(data={"sub": authenticated_user.email})
    
    # función para establecer las cookies
    set_cookies(response, access_token=access_token, refresh_token=refresh_token)
    
    return {
        "id": authenticated_user.id,
        "name": authenticated_user.name,
        "email": authenticated_user.email
    }


from fastapi import APIRouter, Depends, Response, status, Cookie

from app.db.session import get_db
from app.core.versionado import versioned
from app.core.auth import create_access_token, create_refresh_token, set_cookies, verify_token
from app.schemas.user import UserV1, UserResponseV1
from app.schemas.auth import Login, RefreshTokenResponse, VerifyTokenResponse, LogoutResponse
from app.services.user_service import check_user_exists, create_user, authenticate_user
from app.utils.error_handling import raise_unauthorized_error, response_unauthorized_error, response_token_error
from app.core.docs import Docs

router = APIRouter()

@versioned(version="v1")
@router.post("/register", 
             status_code=status.HTTP_201_CREATED, 
             response_model=UserResponseV1,
             description=Docs.registerV1)
def register_user(user_data: UserV1, db=Depends(get_db)):
    
    # Verificar si el usuario ya existe
    check_user_exists(db, user_data.email)
    
    # Crear el usuario
    db_user = create_user(db, user_data.name, user_data.email, user_data.password)
    
    return db_user

@router.post("/login", 
             status_code=status.HTTP_200_OK, 
             response_model=UserResponseV1, 
             responses=response_unauthorized_error(),
             description=Docs.login )
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

@router.post("/refresh_token", 
             status_code=status.HTTP_200_OK, 
             response_model=RefreshTokenResponse, 
             responses=response_token_error(),
             description=Docs.refresh_token)
async def refresh_token(response: Response, refresh_token: str = Cookie(None)):
    
    # Verificar si se proporcionó el refresh token
    if not refresh_token:
        raise_unauthorized_error("No se proporcionó el refresh token")
        
    # Verificar la validez del refresh token
    payload = verify_token(refresh_token)
    if not payload:
        raise_unauthorized_error("Refresh token inválido")
    
    # Extraer el email del payload del refresh token
    email = payload.get("sub")
    if not email:
        raise_unauthorized_error("Refresh token inválido")
    
    # Generar un nuevo access token
    new_access_token = create_access_token(data={"sub": email})
    
    # Establecer el nuevo access token en las cookies
    set_cookies(response, access_token=new_access_token)
    
    return {"message": "Access token renovado exitosamente"}

@router.get("/verify_token", 
            status_code=status.HTTP_200_OK, 
            response_model=VerifyTokenResponse, 
            responses=response_token_error(),
            description=Docs.verify_token)
async def verify(access_token: str = Cookie(None)):
    
    if not access_token:
        raise_unauthorized_error("No se proporcionó el access token")
    
    payload = verify_token(access_token)
    if not payload:
        raise_unauthorized_error("Access token invalido")
    
    return {"message": "Acces token valido", "email": payload.get("sub")}


@router.post("/logout", 
             status_code=status.HTTP_200_OK, 
             response_model=LogoutResponse,
             description=Docs.logout
             )
async def logout(response: Response):

    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    return {"message": "Cerró sesión exitosamente"}
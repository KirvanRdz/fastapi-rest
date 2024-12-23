from fastapi import HTTPException, status

from app.schemas.auth import ErrorAuthResponse, ErrorTokenResponse

def raise_unauthorized_error(detail: str = "Invalid credentials"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )

#funciones que se pueden usar en los decoradores de los endpoints para incluir una respuesta de error 401 
#cuando el token de acceso o el token de actualización no es válido o ha expirado o error de autenticación
def response_unauthorized_error():
    return {
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorAuthResponse,
        }
    }

def response_token_error():
    return {
        status.HTTP_401_UNAUTHORIZED: {
            "model": ErrorTokenResponse,
        }
    }
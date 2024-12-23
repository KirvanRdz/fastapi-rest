from pydantic import BaseModel, EmailStr

class Login(BaseModel):
    email: EmailStr
    password: str

# Respuesta para refresh_token
class RefreshTokenResponse(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Access token renovado exitosamente"
                }
            ]
        }
    }
    

# Respuesta para verify_token
class VerifyTokenResponse(BaseModel):
    message: str
    email: EmailStr

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Access token valido",
                    "email": "juan.perez@example.com"
                }
            ]
        }
    }


# Respuesta para logout
class LogoutResponse(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Cerró sesión exitosamente"
                }
            ]
        }
    }
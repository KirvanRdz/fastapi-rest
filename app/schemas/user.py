from pydantic import BaseModel, EmailStr, field_validator, Field
import re

# Modelos base
class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str 
    
    @field_validator("password") 
    def validate_password(cls, v): 
        if len(v) < 8: raise ValueError("La contraseña debe tener al menos 8 caracteres") 
        if not re.search("[a-zA-Z]", v): raise ValueError("La contraseña debe contener al menos una letra") 
        if not re.search("[0-9]", v): raise ValueError("La contraseña debe contener al menos un número") 
        return v

# Modelos de solicitud para diferentes versiones de la API
class UserV1(UserBase):
    pass

class UserV2(UserBase):
    age: int = Field(ge=18, description="La edad debe ser al menos 18 años.")


# Modelos de respuesta
class UserResponseBase(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserResponseV1(UserResponseBase):
    pass

class UserResponseV2(UserResponseBase):
    age: int
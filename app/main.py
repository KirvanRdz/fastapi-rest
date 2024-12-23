from fastapi import FastAPI

from app.core.config import settings
from app.db.init_db import init_db
from app.api.v1.auth.endpoints import router as auth_router_v1
from app.api.v2.auth.endpoints import router as auth_router_v2

app = FastAPI(
    title="API con Versiones y Autenticación JWT en Cookies", 
    description=(
        "Esta API RESTful, construida con FastAPI, proporciona un sistema de autenticación seguro utilizando JSON Web Tokens (JWT) "
        "almacenados en cookies. Permite la gestión de sesiones de usuario a través de la renovación de tokens y la verificación de la validez de los mismos. "
        "La API soporta múltiples versiones para facilitar la evolución de sus endpoints sin afectar a los clientes existentes. "
        "En la versión 2, se ha añadido un nuevo campo al modelo de usuario para permitir la inclusión de información adicional durante el registro. "
        "Incluye endpoints para el registro de usuarios, inicio de sesión, renovación de tokens, validacion de tokens y cierre de sesión, ofreciendo una solución robusta y escalable para aplicaciones modernas."
    ),
    version="0.0.2",
    debug=settings.DEBUG
)

# Irouters para API v1
app.include_router(auth_router_v1, prefix="/api/v1/auth", tags=["Auth v1"])

# routers para API v2
app.include_router(auth_router_v2, prefix="/api/v2/auth", tags=["Auth v2"])

# Crear las tablas en la base de datos
init_db()

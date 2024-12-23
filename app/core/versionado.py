from app.schemas.user import  UserV1

# Decorador para manejar versiones
def versioned(version: str):
    versions = {
        "v1": UserV1,
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            
            # Extraer los datos de entrada del endpoint
            user_data = kwargs.get("user_data")
            # Validar y transformar los datos según la versión
            user_model = versions.get(version)
            if not user_model:
                raise ValueError(f"Versión no soportada: {version}")
            
            validated_user_data = user_model(**user_data.dict())
            kwargs["user_data"] = validated_user_data
            return func(*args, **kwargs)
        return wrapper
    return decorator


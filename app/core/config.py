from decouple import config

class Settings:
    # Configuración de entorno
    ENVIRONMENT = config("ENVIRONMENT", default="development")  # Por defecto, desarrollo
    
    # Seleccionar la URL de la base de datos según el entorno
    if ENVIRONMENT == "production":
        DATABASE_URL = config("DATABASE_URL_PROD")
    elif ENVIRONMENT == "testing":
        DATABASE_URL = config("DATABASE_URL_TEST")
    else:
        DATABASE_URL = config("DATABASE_URL") 
    

    # Configuración JWT
    SECRET_KEY = config("SECRET_KEY")
    ALGORITHM = config("ALGORITHM", default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)
    REFRESH_TOKEN_EXPIRE_DAYS = config("REFRESH_TOKEN_EXPIRE_DAYS", cast=int, default=30)
    
    # Otros
    DEBUG = config("DEBUG", cast=bool, default=True)

settings = Settings()

from decouple import config

class Settings:
    # Configuración de la base de datos
    DATABASE_URL = config("DATABASE_URL", default="sqlite:///./database.db")

    # Configuración JWT
    SECRET_KEY = config("SECRET_KEY")
    ALGORITHM = config("ALGORITHM", default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)
    REFRESH_TOKEN_EXPIRE_DAYS = config("REFRESH_TOKEN_EXPIRE_DAYS", cast=int, default=30)
    
    # Otros
    DEBUG = config("DEBUG", cast=bool, default=True)

settings = Settings()

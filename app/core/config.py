from decouple import config

class Settings:
    # Configuración de la base de datos
    DATABASE_URL = config("DATABASE_URL", default="sqlite:///./database.db")

    
    # Otros
    DEBUG = config("DEBUG", cast=bool, default=True)

settings = Settings()

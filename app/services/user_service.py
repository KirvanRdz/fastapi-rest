
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import Login
from app.core.auth import get_password_hash, verify_password

# Función para verificar si el usuario ya existe
def check_user_exists(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado",
        )

# Función para crear un nuevo usuario (con edad opcional)
def create_user(db: Session, name: str, email: str, password: str, age: int = None):
    hashed_password = get_password_hash(password)
    db_user = User(name=name, email=email, password=hashed_password, age=age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user: Login):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        return None
    return db_user

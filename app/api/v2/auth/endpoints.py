from fastapi import APIRouter, Depends, status

from app.db.session import get_db
from app.schemas.user import UserV2, UserResponseV2
from app.core.versionado import versioned
from app.services.user_service import check_user_exists, create_user

router = APIRouter()

@versioned(version="v2")
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponseV2)
def register_user_v2(user_data:UserV2, db=Depends(get_db)):
    
    # Verificar si el usuario ya existe
    check_user_exists(db, user_data.email)

    # Crear el usuario con el campo 'age' adicional
    db_user = create_user(db, user_data.name, user_data.email, user_data.password, user_data.age)
    return  db_user

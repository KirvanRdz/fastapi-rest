# utils/error_handling.py
from fastapi import HTTPException, status

def raise_unauthorized_error(detail: str = "Invalid credentials"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )
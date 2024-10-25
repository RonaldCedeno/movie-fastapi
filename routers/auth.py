from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.user_login import User
from utils.jwt_manager import create_token

auth_router = APIRouter()


@auth_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=400, content={"message": "Incorrect user"})

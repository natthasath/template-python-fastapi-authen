from fastapi import APIRouter, Depends, Form, Body
from fastapi.responses import JSONResponse
from app.models.model_auth import UserSchema, UserLoginSchema
from app.services.service_jwt import signJWT, decodeJWT, refreshJWT

router = APIRouter(
    prefix="/auth",
    tags=["AUTHENTICATION"],
    responses={404: {"message": "Not found"}}
)

users = []

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@router.post("/user/signup")
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)

@router.post("/user/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
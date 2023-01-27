from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.models.model_auth import PostSchema, UserSchema, UserLoginSchema
from app.services.service_authen import JWTBearer

router = APIRouter(
    prefix="",
    tags=["POSTS"],
    responses={404: {"message": "Not found"}}
)

posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]

users = []

@router.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to your blog!."}

@router.get("/posts", dependencies=[Depends(JWTBearer())])
async def get_posts() -> dict:
    return { "data": posts }


@router.get("/posts/{id}", dependencies=[Depends(JWTBearer())])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

@router.post("/posts", dependencies=[Depends(JWTBearer())])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }
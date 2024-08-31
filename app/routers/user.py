from fastapi import APIRouter
from app import schemas
import os

router = APIRouter()

@router.post('/me', response_model=schemas.UserResponseSchema)
def post_me(user: schemas.UserRequestSchema):
    name, age, location = user.name, user.age, user.location
    mongo_uri = os.getenv("DATABASE_URI")
    welcome_str = f"Welcome {name}, {age} years old from {location}. Also your MongoDB URI is {mongo_uri}."
    return {"res": welcome_str, "user": user}

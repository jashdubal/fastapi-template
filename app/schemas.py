from pydantic import BaseModel


class UserRequestSchema(BaseModel):
    name: str
    age: int
    location: str

class UserResponseSchema(BaseModel):
    res: str
    user: UserRequestSchema

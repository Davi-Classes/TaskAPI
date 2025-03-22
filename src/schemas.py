from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str


class MessageOut(BaseModel):
    message: str
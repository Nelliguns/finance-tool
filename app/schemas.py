from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True



class HolderData(BaseModel):
    company: list
    holding: list

    class Config:
        orm_mode = True


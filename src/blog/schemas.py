from pydantic import BaseModel


class BasePost(BaseModel):
    title: str
    body: str


class CreatePost(BasePost):
    class Config:
        orm_mode = True


class UpdatePost(BasePost):
    class Config:
        orm_mode = True


from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str
    last_name: str = None
    age:  int = Field(
        43,
        title='Возраст',
        description='',
        gt=1,
        lt=100,
    )

    class Config:
        orm_mode = True


class UserWithID(User):
    id: int


class AnyUserWithID(UserWithID):
    age: int

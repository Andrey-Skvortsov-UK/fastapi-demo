from typing import List

from fastapi import APIRouter

from fastapi_demo import schema, models

api_router = APIRouter()


@api_router.get("/users/", response_model=List[schema.AnyUserWithID])
def get_users():
    return list(models.User.all())


@api_router.post("/user/", response_model=schema.UserWithID, status_code=201)
async def create_user(user: schema.User):
    user = models.User.create(**user.dict())
    return user


@api_router.put("/user/", response_model=schema.UserWithID)
async def update_user(user_id: int, user: schema.User):
    user = models.User.find_or_fail(id_=user_id).update(**user.dict())
    return user


@api_router.delete("/user/", status_code=204)
async def delete_user(user_id: int):
    models.User.find_or_fail(id_=user_id).delete()

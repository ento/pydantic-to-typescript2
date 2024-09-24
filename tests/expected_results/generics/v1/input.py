from datetime import datetime
from typing import Generic, List, Optional, Type, TypeVar, cast

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class Error(BaseModel):
    code: int
    message: str


class ApiResponse(GenericModel, Generic[T]):
    data: Optional[T]
    error: Optional[Error]


def create_response_type(data_type: T, name: str) -> "Type[ApiResponse[T]]":
    """
    Create a concrete implementation of ApiResponse and then applies the specified name.
    This is necessary because the name automatically generated by __concrete_name__ is
    really ugly, it just doesn't look good.
    """
    t = ApiResponse[data_type]
    t.__name__ = name
    t.__qualname__ = name
    return cast(Type[ApiResponse[T]], t)


class User(BaseModel):
    name: str
    email: str


class UserProfile(User):
    joined: datetime
    last_active: datetime
    age: int


class Article(BaseModel):
    author: User
    content: str
    published: datetime


ListUsersResponse = create_response_type(List[User], "ListUsersResponse")

ListArticlesResponse = create_response_type(List[Article], "ListArticlesResponse")

UserProfileResponse = create_response_type(UserProfile, "UserProfileResponse")

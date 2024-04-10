from typing import Optional

from pydantic import BaseModel, Field


class RoleDTO(BaseModel):
    pk: int
    name: str
    color: str


class UserBaseDTO(BaseModel):
    username: str = Field(max_length=20, min_length=2)
    last_name: Optional[str] = Field(max_length=20, default=None)
    email: str = Field(max_length=100, min_length=5)
    telegram_name: str = Field(max_length=50, min_length=2)
    telegram_nick: str = Field(max_length=50, min_length=2)
    google_meet_nick: str = Field(max_length=50, min_length=2)
    gitlab_nick: str = Field(max_length=50, min_length=2)
    github_nick: str = Field(max_length=50, min_length=2)


class CreateUserDTO(UserBaseDTO):
    password: str = Field(max_length=150, min_length=8)
    role_id: int


class UpdateUserDTO(UserBaseDTO):
    ...


class CreateAdminDTO(CreateUserDTO):
    role: RoleDTO


class UpdateAdminDTO(CreateAdminDTO):
    ...


class UserDTO(UserBaseDTO):
    id: int
    role: RoleDTO


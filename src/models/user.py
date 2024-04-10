from datetime import datetime
from typing import TYPE_CHECKING
import edgy

from .base import BaseModel
# from esmerald.contrib.auth.edgy.base_user import User as BaseUser
# from .permission import PermissionModel
# from .user_permission import UserPermissionModel
from .role import RoleModel

# if TYPE_CHECKING:


class UserModel(BaseModel):

    username: str = edgy.CharField(max_length=20)
    last_name: str = edgy.CharField(max_length=20, null=True)
    email: str = edgy.EmailField(max_length=100, min_length=5, unique=True)
    password: str = edgy.PasswordField(max_length=150, min_length=8)
    telegram_name: str = edgy.CharField(max_length=50)
    telegram_nick: str = edgy.CharField(max_length=50)
    google_meet_nick: str = edgy.CharField(max_length=50)
    gitlab_nick: str = edgy.CharField(max_length=50)
    github_nick: str = edgy.CharField(max_length=50)
    is_active: bool = edgy.BooleanField(default=False)
    is_admin: bool = edgy.BooleanField(default=False)
    avatar: str = edgy.CharField(max_length=500, null=True)
    last_login: datetime = edgy.DateTimeField(null=True)
    role: "RoleModel" = edgy.ForeignKey(RoleModel, on_delete=edgy.CASCADE, related_name="users")
    # permissions: list["PermissionModel"] = edgy.ManyToMany(
    #     PermissionModel,
    #     through=UserPermissionModel,
    #     related_name="users"
    # )

    class Meta:
        tablename = "users"

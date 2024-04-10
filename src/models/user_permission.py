from typing import TYPE_CHECKING

import edgy

from .base import BaseModel

# if TYPE_CHECKING:
from .permission import PermissionModel
from .user import UserModel


class UserPermissionModel(BaseModel):

    permission: "PermissionModel" = edgy.ForeignKey(PermissionModel , on_delete=edgy.CASCADE)
    user: "UserModel" = edgy.ForeignKey(UserModel, on_delete=edgy.CASCADE)

    class Meta:
        tablename = "user_permissions"

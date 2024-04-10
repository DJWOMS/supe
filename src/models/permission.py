import edgy

from .base import BaseModel


class PermissionModel(BaseModel):

    name: str = edgy.CharField(unique=True, max_length=255)
    code: int = edgy.IntegerField(unique=True, minimum=6, maximum=6)
    description: str = edgy.CharField(max_length=255, null=True)

    class Meta:
        tablename = "permissions"


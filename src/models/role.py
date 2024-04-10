import edgy

from .base import BaseModel


class RoleModel(BaseModel):

    name: str = edgy.CharField(max_length=20)
    color: str = edgy.CharField(max_length=6, default='#000000')

    class Meta:
        tablename = 'roles'

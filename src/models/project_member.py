import edgy

from .base import BaseModel


class ProjectMemberModel(BaseModel):

    project: int = edgy.ForeignKey("ProjectModel", on_delete=edgy.CASCADE)
    user: int = edgy.ForeignKey("UserModel", on_delete=edgy.CASCADE)

    class Meta:
        table = "members"

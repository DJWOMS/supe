import edgy

from .base import BaseModel

from src.apps.project.constants import StatusProject


class ProjectModel(BaseModel):

    name: str = edgy.CharField(max_length=100)
    description: str = edgy.CharField(max_length=1000, null=True)
    status: StatusProject = edgy.ChoiceField(choices=StatusProject, default=StatusProject.ACTIVE)
    logo: str = edgy.CharField(max_length=500, null=True)
    members: list["UserModel"] = edgy.ManyToManyField(
        "UserModel",
        through="ProjectMemberModel",
        related_name="projects"
    )

    class Meta:
        tablename = "projects"

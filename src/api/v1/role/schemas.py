from pydantic import BaseModel


class RoleBaseSchema(BaseModel):
    name: str
    color: str


class CreateRoleSchema(RoleBaseSchema):
    ...


class UpdateRoleSchema(RoleBaseSchema):
    ...


class RoleSchema(RoleBaseSchema):
    id: int

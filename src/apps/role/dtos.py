from dataclasses import dataclass, field

from src.lib.dto import BaseDTO


@dataclass
class CreateRoleDTO(BaseDTO):
    name: str = field(metadata={"min_length": 3, "max_length": 20})
    color: str = field(metadata={"min_length": 6, "max_length": 6})


@dataclass
class UpdateRoleDTO(CreateRoleDTO):
    ...


@dataclass
class RoleDTO(CreateRoleDTO):
    id: int


@dataclass
class RoleDTOTest(CreateRoleDTO):
    ...

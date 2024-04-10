from esmerald import AsyncDAOProtocol

from src.apps.role.dtos import CreateRoleDTO, RoleDTO
from src.models import RoleModel


class RoleRepository:
    model = RoleModel

    async def create(self, dto: CreateRoleDTO):
        return await self.model.query.create(**dto.model_dump())
    
    async def get(self, pk: int) -> RoleDTO:
        return await self.model.query.get(id=pk)

    async def get_by_name(self, name: str) -> RoleDTO:
        return await self.model.query.get(name=name)

    async def get_all(self):
        return await self.model.query.all()

    async def update(self, pk: int, dto: CreateRoleDTO):
        return await self.model.query.filter(id=pk).update(**dto.model_dump())

    async def delete(self, pk: int):
        return await self.model.query.filter(id=pk).delete()

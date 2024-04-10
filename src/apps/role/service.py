from .dtos import CreateRoleDTO, RoleDTO
from .repository import RoleRepository


class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    async def create(self, dto: CreateRoleDTO) -> RoleDTO:
        return await self.repository.create(dto)

    async def get_by_id(self, pk: int) -> RoleDTO:
        return await self.repository.get(pk)

    async def get_by_name(self, name: str) -> RoleDTO:
        return await self.repository.get_by_name(name)

    async def get_all(self) -> list[RoleDTO]:
        return await self.repository.get_all()

    async def update(self, pk: int, dto: CreateRoleDTO) -> RoleDTO:
        return await self.repository.update(pk, dto)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)

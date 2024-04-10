from src.apps.user.dtos import CreateAdminDTO, UpdateAdminDTO, UserDTO
from src.models.user import UserModel


class AdminRepository:
    model = UserModel

    async def create(self, dto: CreateAdminDTO, is_admin: bool, is_active: bool) -> UserDTO:
        return await self.model.query.create(
            **dto.model_dump(exclude={"role"}), role=dto.role, is_admin=is_admin, is_active=is_active
        )

    async def get(self, pk: int) -> UserDTO:
        return await self.model.query.get(id=pk)

    async def get_all(self) -> list[UserDTO]:
        return await self.model.query.all()

    async def update(self, pk: int, dto: UpdateAdminDTO) -> UserDTO:
        return await self.model.query.filter(id=pk).update(**dto.model_dump())

    async def delete(self, pk: int):
        return await self.model.query.filter(id=pk).delete()

from src.apps.user.dtos import CreateUserDTO, UpdateUserDTO, UserDTO
from src.models.user import UserModel


class UserRepository:
    model = UserModel

    async def create(self, dto: CreateUserDTO, role) -> UserModel:
        return await self.model.query.create(**dto.model_dump(exclude={"role_id"}), role=role)
    
    async def get(self, pk: int) -> UserDTO:
        return await self.model.query.get(id=pk)

    async def get_all(self) -> list[UserDTO]:
        return await self.model.query.all()

    async def update(self, pk: int, dto: UpdateUserDTO) -> UserDTO:
        return await self.model.query.filter(id=pk).update(**dto.model_dump())

    async def delete(self, pk: int):
        return await self.model.query.filter(id=pk).delete()

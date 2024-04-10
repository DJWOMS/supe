from src.models import UserModel
from ..dtos import CreateUserDTO, UpdateUserDTO, CreateAdminDTO, UpdateAdminDTO, UserDTO
from ..commands import UserCreateCommand, AdminCreateCommand
from ..repositories import UserRepository
from ...role.repository import RoleRepository


class UserService:
    def __init__(self, repository: UserRepository, role_repository: RoleRepository):
        self.repository = repository
        self.role_repository = role_repository

    async def create_user(self, dto: CreateUserDTO) -> UserModel:
        if role := await self.role_repository.get(dto.role_id):
            print("111"*100)
            print(role)
            return await self.repository.create(dto, role)

    async def create_admin(self, dto: CreateAdminDTO) -> UserDTO:
        return await AdminCreateCommand(self.repository.create_admin(dto))

    async def get_user_by_id(self, pk: int) -> UserDTO:
        return await self.repository.get(pk)

    async def get_all_users(self) -> list[UserDTO]:
        return await self.repository.get_all()

    async def update_user(self, pk: int, dto: UpdateUserDTO) -> UserDTO:
        return await self.repository.update(pk, dto)

    async def delete_user(self, pk: int):
        return await self.repository.delete(pk)

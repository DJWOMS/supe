from typing import TYPE_CHECKING

from src.apps.user.dtos import CreateAdminDTO, UserDTO

if TYPE_CHECKING:
    from src.apps.user.repositories import AdminRepository


class AdminCreateCommand:
    def __init__(self, admin_repository: "AdminRepository"):
        self.repository = admin_repository

    async def create_admin(self, dto: CreateAdminDTO) -> UserDTO:
        return await self.repository.create(dto, is_admin=True, is_active=True)

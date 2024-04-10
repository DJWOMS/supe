from src.apps.user.dtos import CreateUserDTO


class UserCreateCommand:
    def __init__(self, user_repository):
        self.repository = user_repository

    async def execute(self, dto: CreateUserDTO):
        return await self.repository.create(dto)

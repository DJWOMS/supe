from esmerald import post, APIView, Inject, get, put, delete, status

from src.apps.role.repository import RoleRepository
from src.apps.user.repositories import UserRepository
from src.apps.user.services.user_service import UserService
from src.models import UserModel, PermissionModel
from src.apps.user.dtos import UserDTO, CreateUserDTO


class UserAPIView(APIView):
    path = "/"
    tags = ["User"]
    dependencies = {
        "repository": Inject(UserRepository),
        "role_repository": Inject(RoleRepository),
        "service": Inject(UserService),
    }

    @post(path="/", summary="Create user", status_code=status.HTTP_201_CREATED)
    async def create(self, data: CreateUserDTO, service: UserService) -> UserModel:
        print("222"*100)
        return await service.create_user(data)

    # @get("/{pk}")
    # async def get_by_id(self, pk: int) -> ...:
    #     ...
    #
    # @get("/", summary="Get all users", status_code=status.HTTP_200_OK)
    # async def get_all(self, service: UserService) -> list[UserDTO]:
    #     return await service.get_all_users()
    #
    # @put("/{pk}")
    # async def update(self, pk: int) -> ...:
    #     ...
    #
    # @delete("/{pk}", status_code=status.HTTP_204_NO_CONTENT)
    # async def delete(self, pk: int) -> ...:
    #     ...

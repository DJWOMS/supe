from esmerald import post, APIView, Inject, get, put, delete, status, Factory

from src.apps.role.dtos import CreateRoleDTO, UpdateRoleDTO, RoleDTO
from src.apps.role.repository import RoleRepository
# from .schemas import CreateRoleSchema, UpdateRoleSchema

from src.apps.role.service import RoleService


class RoleAPIView(APIView):
    # path = "/roles"
    tags = ["Role"]
    dependencies = {
        "repository": Inject(RoleRepository),
        "service": Inject(RoleService)
    }

    @post("/", summary="Create role", status_code=status.HTTP_201_CREATED)
    async def create(self, data: CreateRoleDTO, service: RoleService) -> RoleDTO:
        return await service.create(data)

    @get("/{pk:int}", summary="Get role by id")
    async def get_by_id(self, pk: int, service: RoleService) -> RoleDTO:
        return await service.get_by_id(pk)

    @get("/", summary="Get all roles")
    async def get_all(self, service: RoleService) -> list[RoleDTO]:
        return await service.get_all()

    @put("/{pk:int}", summary="Update role by id")
    async def update(self, pk: int, data: UpdateRoleDTO, service: RoleService) -> RoleDTO:
        return await service.update(pk, data)

    @delete("/{pk:int}", summary="Delete role by id", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(self, pk: int, service: RoleService) -> None:
        return await service.delete(pk)

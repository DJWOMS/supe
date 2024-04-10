import argparse
from typing import Any, Type

import edgy
from asyncpg import UniqueViolationError
from esmerald.core.directives import BaseDirective
from esmerald.core.terminal import Print

from src.apps.role.dtos import CreateRoleDTO
from src.apps.role.repository import RoleRepository
from src.apps.role.service import RoleService
from src.apps.user.commands import AdminCreateCommand
from src.apps.user.dtos import CreateAdminDTO, RoleDTO
from src.apps.user.repositories import AdminRepository


class Directive(BaseDirective):
    help: str = "Creates a superuser"

    def add_arguments(self, parser: Type["argparse.ArgumentParser"]) -> Any:
        parser.add_argument("--username", dest="username", type=str, required=True)
        parser.add_argument("--email", dest="email", type=str, required=True)
        parser.add_argument("--password", dest="password", type=str, required=True)

    async def get_role(self):
        role_service = RoleService(RoleRepository())
        try:
            role = await role_service.get_by_name("admin")
        except edgy.exceptions.ObjectNotFound:
            role = await role_service.create(CreateRoleDTO(name="admin", color="000000"))

        return RoleDTO(pk=role.id, name=role.name, color=role.color)

    async def handle(self, *args: Any, **options: Any) -> Any:
        """Generates an admin"""
        printer = Print()

        username = options["username"]
        email = options["email"]
        password = options["password"]

        role = await self.get_role()

        user = CreateAdminDTO(
            username=username,
            last_name=username,
            email=email,
            password=password,
            telegram_name=username,
            telegram_nick=username,
            google_meet_nick=username,
            gitlab_nick=username,
            github_nick=username,
            role=role,
        )

        command = AdminCreateCommand(AdminRepository())

        try:
            user = await command.create_admin(user)
        except UniqueViolationError:
            printer.write_error(f"User with email {email} already exists.")
            return

        printer.write_success(f"Superuser {user.email} created successfully.")

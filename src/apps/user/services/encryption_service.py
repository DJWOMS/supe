import random
import string

from argon2 import PasswordHasher

from esmerald.conf import settings


class EncryptionService:
    salt: str = settings.salt
    length_password: int = 8

    def get_new_hashed_password(self) -> str:
        password = self.generate_password()
        return self.create_hash_password(password)

    def generate_password(self, length_password: int | None = None) -> str:
        if length_password is None:
            length_password = self.length_password

        rand_pass = ''.join(
            random.choices(
                f"{string.ascii_lowercase}{string.ascii_uppercase}{string.digits}",
                k=length_password)
        )
        return rand_pass

    def create_hash_password(self, password: str) -> str:
        return PasswordHasher().hash(password.encode("utf-8"), salt=self.salt.encode("utf-8"))

from typing import Optional, Annotated

from esmerald.conf.enums import EnvironmentType
from esmerald.conf.global_settings import EsmeraldAPISettings

from src.configs.databse import DataBaseSettings


class AppSettings(DataBaseSettings):
    app_name: str = "My application in production mode."
    title: str = "My config"
    environment: Optional[str] = EnvironmentType.PRODUCTION
    secret_key: str = "esmerald-insecure-87uq__0ketos&amp;42*y9p669=dm7jfug1b8@07&amp;ze4+8@sl+$t@d"
    salt: str = "esmerald-insecure-87uq__0ketos&amp;42*y9p669=dm7jfug1b8@07&amp;ze4+8@sl+$t@d"
    access_token_expire_minutes: int = 60
    algorithm: str = "HS256"

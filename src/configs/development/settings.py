from typing import Optional, Annotated

from esmerald.conf.enums import EnvironmentType

from ..settings import AppSettings


class DevelopmentAppSettings(AppSettings):
    debug: bool = True
    app_name: str = "My application in development mode."
    title: str = "My config"
    environment: Optional[str] = EnvironmentType.DEVELOPMENT

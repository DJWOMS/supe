from typing import Optional

from esmerald.conf.enums import EnvironmentType

from ..settings import AppSettings


class TestingAppSettings(AppSettings):
    debug: bool = True
    app_name: str = "My application in testing mode."
    title: str = "My config"
    environment: Optional[str] = EnvironmentType.TESTING

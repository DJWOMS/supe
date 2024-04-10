from functools import cached_property

from edgy import Database, Registry
from esmerald import EsmeraldAPISettings
from pydantic import Field


class DataBaseSettings(EsmeraldAPISettings):
    user: str = Field(..., alias="POSTGRES_USER")
    password: str = Field(..., alias="POSTGRES_PASSWORD")
    host: str = Field(..., alias="POSTGRES_HOST")
    port: str = Field(..., alias="POSTGRES_PORT")
    url_schema: str = Field("postgresql+asyncpg", alias="DB_URL_SCHEME")
    name: str = Field(..., alias="POSTGRES_DB")

    @cached_property
    def registry(self) -> tuple[Database, Registry]:
        database = Database(self.url)
        return database, Registry(database=database)

    @property
    def url(self) -> str:
        return f"{self.url_schema}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

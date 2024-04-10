from typing import Optional, Annotated

from esmerald.conf.enums import EnvironmentType

from ..settings import AppSettings


class DevelopmentAppSettings(AppSettings):
    debug: bool = True
    app_name: str = "My application in development mode."
    title: str = "My config"
    environment: Optional[str] = EnvironmentType.DEVELOPMENT
    swagger_js_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.14.0/swagger-ui-bundle.js"
    # swagger_css_url: str = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.15.0/swagger-ui.css"

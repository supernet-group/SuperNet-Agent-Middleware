from pydantic_settings import BaseSettings

class StaticConfig:
    # API-PREFIX
    PREFIX_SUPERNET_AGENT_MANAGER = "/manager"
    PREFIX_SUPERNET_AGENT_CLIENT = "/client"

    # API-SUPERNET-AGENT-BACKEND-PREFIX
    PREFIX_SAB_CREATE = "/create"

    # REQUEST-METHODS
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"

class DynamicConfig(BaseSettings):
    # SUPERNET-AGENT-BACKEND-URL
    SUPERNET_AGENT_BACKEND_URL: str = "http://localhost:8080"

    DEBUG_MODE: bool = False

    class Config:
        env_file = ".env"

static_config = StaticConfig()
dynamic_config = DynamicConfig()

from pydantic import BaseSettings

class StaticConfig:
    # API-PREFIX
    PREFIX_SUPERNET_AGENT_MANAGER = "/manager"
    PREFIX_SUPERNET_AGENT_CLIENT = "/client"

class DynamicConfig(BaseSettings):
    # SUPERNET-AGENT-BACKEND-URL
    SUPERNET_AGENT_BACKEND_URL: str = "http://localhost:8080"

    class Config:
        env_file = ".env"

static_config = StaticConfig()
dynamic_config = DynamicConfig()

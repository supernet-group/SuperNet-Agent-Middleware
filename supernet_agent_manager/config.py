class ManagerConfig:

    # API-SUPERNET-AGENT-BACKEND-PREFIX
    # SAB is the name of the SUPERNET-AGENT-BACKEND
    # Auth
    API_SAB_REFRESH_TOKEN = "/refresh-token"
    API_SAB_LOGIN = "/login"

    # Agent
    API_SAB_AGENTS = "/apps"
    API_SAB_AGENTS_IMPORTS = "/apps/imports"
    API_SAB_AGENTS_EXPORTS = "/exports"
    
    # Tag
    API_SAB_TAGS = "/tags"
    API_SAB_TAGS_BIND = "/tag-bindings/create"

static_config = ManagerConfig()

class ManagerConfig:

    # API-SUPERNET-AGENT-BACKEND-PREFIX
    # SAB is the name of the SUPERNET-AGENT-BACKEND
    # Auth
    API_SAB_REFRESH_TOKEN = "/refresh-token"
    API_SAB_LOGIN = "/login"

    # Agent
    API_SAB_AGENTS_CREATE = "/create-agent"
    API_SAB_AGENTS_LIST = "/list-agent"
    API_SAB_AGENTS_DETAIL = "/detail-agent"
    API_SAB_AGENTS_UPDATE = "/detail-agent"
    API_SAB_AGENTS_DELETE = "/detail-agent"
    API_SAB_AGENTS_COPY = "/start-agent"
    
    # Tag
    API_SAB_TAGS = "/tag"
    API_SAB_TAGS_LIST = "/list-tags"
    API_SAB_TAGS_BIND = "/tag-bindings/create"

static_config = ManagerConfig()

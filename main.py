from fastapi import FastAPI
from common.config import static_config
from supernet_agent_manager.api.auth import router as auth_router
from supernet_agent_manager.api.agent import router as agent_router
from supernet_agent_manager.api.tag import router as tag_router
from supernet_agent_client.api.chat import router as chat_router

app = FastAPI()

app.include_router(auth_router, prefix=static_config.PREFIX_SUPERNET_AGENT_MANAGER, tags=["Authorization"])
app.include_router(agent_router, prefix=static_config.PREFIX_SUPERNET_AGENT_MANAGER, tags=["Agent"])
app.include_router(tag_router, prefix=static_config.PREFIX_SUPERNET_AGENT_MANAGER, tags=["Tag"])

app.include_router(chat_router, prefix=static_config.PREFIX_SUPERNET_AGENT_CLIENT, tags=["Chat"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Scaffold!"}
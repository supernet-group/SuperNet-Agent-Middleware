from fastapi import FastAPI
from common.config import static_config
from supernet_agent_manager.api.endpoints import router as router_manager

app = FastAPI()

app.include_router(router_manager, prefix=static_config.PREFIX_SUPERNET_AGENT_MANAGER, tags=["Module agent manager"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Scaffold!"}
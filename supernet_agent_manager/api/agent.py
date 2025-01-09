from fastapi import APIRouter,Request
from common.logger import logger
from ..model.create_agent import CreateAgent
from  ..service.agent_service import AgentService

router = APIRouter()

# create_agent
@router.post("/create-agent")
async def create_agent(create_agent_req: CreateAgent, request: Request):
    logger.info("create_agent_req: %s", create_agent_req)
    access_token = request.headers.get("Authorization")
    return await AgentService.create_agent(create_agent_req, access_token)

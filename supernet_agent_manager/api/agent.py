from fastapi import APIRouter
from common.logger import logger
from ..model.create_agent import CreateAgent
from  ..service.agent_service import AgentService

router = APIRouter()

# create_agent
@router.post("/create-agent")
async def create_agent(create_agent_req: CreateAgent):
    logger.info("create_agent_req: %s", create_agent_req)
    return await AgentService.create_agent(create_agent_req)

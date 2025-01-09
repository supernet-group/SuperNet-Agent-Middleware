from fastapi import APIRouter,Request
from common.logger import logger
from ..model.create_agent import CreateAgent
from ..model.list_agents import ListAgents
from  ..service.agent_service import AgentService

router = APIRouter()

# create_agent
@router.post("/create-agent")
async def create_agent(create_agent_req: CreateAgent, request: Request):
    logger.info("create_agent_req: %s", create_agent_req)
    access_token = request.headers.get("Authorization")
    return await AgentService.create_agent(create_agent_req, access_token)

# list_agents
@router.get("/list-agents")
async def list_agents(request: Request):
    query_params = request.query_params
    list_agents_req = ListAgents(
        name=query_params.get("name"),
        page=int(query_params.get("page")),
        limit=int(query_params.get("limit"))
    )
    logger.info("list_agents_req: %s", list_agents_req)
    access_token = request.headers.get("Authorization")
    return await AgentService.list_agents(list_agents_req, access_token)

from fastapi import APIRouter,Request, HTTPException, status
from fastapi.responses import JSONResponse
from common.logger import logger
from ..model.create_agent import CreateAgent
from ..model.list_agents import ListAgents
from ..model.banding_tag import BindingTag
from ..service.agent_service import AgentService
from ..service.tag_service import TagService

router = APIRouter()

@router.post("/create-agent")
async def create_agent(create_agent_req: CreateAgent, request: Request):
    """
    Description: Create agent
    Args:
        create_agent_req (CreateAgent): Create agent request
        request (Request): Http Request object
    Returns:
        JSON
    """
    logger.info("create_agent_req: %s", create_agent_req)
    access_token = request.headers.get("Authorization")
    # Generate no-tag agent
    try:
        base_agent_resp = await AgentService.create_agent(create_agent_req, access_token)
    except Exception as e:
        logger.error("Failed to create agent: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create agent")

    # Bind tags
    if create_agent_req.tags and not isinstance(base_agent_resp, JSONResponse):
        try:
            bind_tag_req = BindingTag(
                target_id=base_agent_resp['id'],
                tag_ids=create_agent_req.tags,
            )
            bind_tag_resp = await TagService.bind_tag(
                binding_tag_req=bind_tag_req,
                access_token=access_token
            )
            logger.info("bind_tag_resp: %s", bind_tag_resp)
        except Exception as e:
            await rollback_agent_creation(base_agent_resp, access_token)
            logger.error("Failed to bind tags: %s", str(e))
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to bind tags")

    return base_agent_resp

# list_agents
@router.get("/list-agents")
async def list_agents(request: Request):
    """
    Description: List agents
    Args:
        request (Request): Http Request object
    Returns:
        JSON
    """
    query_params = request.query_params
    list_agents_req = ListAgents(
        name=query_params.get("name"),
        page=int(query_params.get("page")),
        limit=int(query_params.get("limit"))
    )
    logger.info("list_agents_req: %s", list_agents_req)
    access_token = request.headers.get("Authorization")
    return await AgentService.list_agents(list_agents_req, access_token)

# rollback_agent_creation
async def rollback_agent_creation(base_agent_resp, access_token):
    """
    Description: Rollback agent creation due to tag binding failure
    Args:
        base_agent_resp (JSON): Base agent response
        access_token (str): Access token
    Returns:
        None
    """
    try:
        await AgentService.delete_agent(base_agent_resp['id'], access_token)
        logger.info("Rollback: Deleted agent %s due to tag binding failure", base_agent_resp['id'])
    except Exception as delete_error:
        logger.error("Failed to delete agent during rollback: %s. Agent ID: %s", str(delete_error), base_agent_resp.get('id', 'unknown'))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to rollback agent creation")
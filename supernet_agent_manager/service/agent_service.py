from common.service.call_generic_api import call
from common.model.generic_api_request import GenericAPIRequest
from common.config import static_config, dynamic_config
from ..config import ManagerConfig
from ..model.create_agent import CreateAgent
from ..model.list_agents import ListAgents

class AgentService: 
    @staticmethod
    async def create_agent(create_agent_req: CreateAgent, access_token: str):
        headers = {}
        headers["Authorization"] = access_token
        headers["Content-Type"] = "application/json"
        url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_AGENTS
        if create_agent_req.mode == "yaml-content":
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_AGENTS_IMPORTS

        # generate base agent
        return await call(GenericAPIRequest(
            method=static_config.POST,
            headers=headers,
            url=url,
            json_data=create_agent_req.model_dump()
        ))
    
    @staticmethod
    async def list_agents(list_agents_req: ListAgents, access_token: str):
        headers = {}
        headers["Authorization"] = access_token
        headers["Content-Type"] = "application/json"

        return await call(GenericAPIRequest(
            method=static_config.GET,
            headers=headers,
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_AGENTS,
            params=list_agents_req.model_dump()
        ))
    
    @staticmethod
    async def delete_agent(agent_id: str, access_token: str):
        headers = {}
        headers["Authorization"] = access_token
        headers["Content-Type"] = "application/json"

        return await call(GenericAPIRequest(
            method=static_config.DELETE,
            headers=headers,
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_AGENTS + "/" + agent_id
        ))
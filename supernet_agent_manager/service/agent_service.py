from common.service.call_generic_api import call
from common.model.generic_api_request import GenericAPIRequest
from common.config import static_config, dynamic_config
from ..config import ManagerConfig
from ..model.create_agent import CreateAgent

class AgentService: 
    @staticmethod
    async def create_agent(create_agent_req: CreateAgent, access_token: str):
        headers = {}
        headers["Authorization"] = access_token
        headers["Content-Type"] = "application/json"
        return await call(GenericAPIRequest(
            method=static_config.POST,
            headers=headers,
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_AGENTS_CREATE,
            json_data=create_agent_req.model_dump()  
        ))
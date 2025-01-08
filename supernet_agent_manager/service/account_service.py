from common.service.call_generic_api import call
from common.model.generic_api_request import GenericAPIRequest
from common.config import static_config, dynamic_config
from ..model.refresh_token import RefreshToken
from ..model.login import Login
from ..config import ManagerConfig

class AccountService:

    @staticmethod
    async def refresh_token(refresh_token_req: RefreshToken):
        return await call(GenericAPIRequest(
            method=static_config.POST,
            headers={"Content-Type": "application/json"},
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_REFRESH_TOKEN,
            json_data=refresh_token_req.model_dump(),
        ))
    
    @staticmethod
    async def login(login_req: Login):
        return await call(GenericAPIRequest(
            method=static_config.POST,
            headers={"Content-Type": "application/json"},
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_LOGIN,
            json_data=login_req.model_dump(),
        ))
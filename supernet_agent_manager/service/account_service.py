from common.service.call_generic_api import call
from common.model.generic_api_request import GenericAPIRequest
from ..model.refresh_token import RefreshToken
from ..config import ManagerConfig
from common.config import dynamic_config

class AccountService:

    @staticmethod
    def refresh_account_info(refresh_token_req : RefreshToken):
        return call(GenericAPIRequest(
            method="POST",
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_REFRESH_TOKEN,
            json={"refresh_token": refresh_token_req.refresh_token},
        ))
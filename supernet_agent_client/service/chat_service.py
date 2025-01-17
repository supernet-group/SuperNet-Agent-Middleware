from common.config import static_config, dynamic_config
from common.model.generic_api_request import GenericAPIRequest
from common.service.call_generic_api import stream_call
from common.logger import logger
from ..config import ClientConfig
from ..model.chat import Chat


class ChatService:
    @staticmethod
    async def debug_chat(chat:Chat, access_token: str):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{access_token}"
        }
        logger.info(f"Sending DEBUG chat to {chat.config}")   
        url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ClientConfig.API_SAC_AGENT_PREFIX.format(appId=chat.config['appId'])
        logger.info(f"Sending DEBUG chat to {url}")

        json_data = chat.model_dump()
        json_data['model_config'] = json_data['config']

        logger.info(f"Sending DEBUG chat to {json_data}")

        return await stream_call(GenericAPIRequest(
            url=url,
            method=static_config.POST,
            headers=headers,
            json_data=json_data
        ))
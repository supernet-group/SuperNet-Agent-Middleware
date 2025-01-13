from common.config import static_config, dynamic_config
from common.model.generic_api_request import GenericAPIRequest
from common.service.call_generic_api import stream_call

from ..config import ClientConfig
from ..model.chat import Chat


class ChatService:
    @staticmethod
    async def debug_chat(chat:Chat, access_token: str):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        return await stream_call(GenericAPIRequest(
            method=static_config.POST,
            headers=headers,
            json_data=chat.model_dump()
        ))
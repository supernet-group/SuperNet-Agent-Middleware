from common.service.call_generic_api import call
from common.model.generic_api_request import GenericAPIRequest
from common.config import static_config, dynamic_config
from ..model.tag import Tag
from ..model.banding_tag import BindingTag
from ..config import ManagerConfig



class TagService:
    @staticmethod
    async def create_tag(tag_req: Tag):
        tag_req_json = tag_req.model_dump()
        tag_req_json["type"] = "app"
        return await call(GenericAPIRequest(
            method=static_config.POST,
            headers={"Content-Type": "application/json"},
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_TAGS,
            json_data=tag_req_json  
        ))
    
    @staticmethod
    async def get_tags():
        tag_req_json = {}
        tag_req_json["type"] = "app"
        return await call(GenericAPIRequest(
            method=static_config.GET,
            headers={"Content-Type": "application/json"},
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_TAGS_LIST,
            params=tag_req_json
        ))
    
    @staticmethod
    async def bind_tag(binding_tag_req: BindingTag):
        return await call(GenericAPIRequest(
            method=static_config.POST,
            headers={"Content-Type": "application/json"},
            url=dynamic_config.SUPERNET_AGENT_BACKEND_URL + ManagerConfig.API_SAB_TAGS_BIND,
            json_data=binding_tag_req.model_dump()
        ))
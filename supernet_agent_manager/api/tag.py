from fastapi import APIRouter
from common.logger import logger
from ..model.tag import Tag
from ..model.banding_tag import BindingTag
from ..service.tag_service import TagService

router = APIRouter()

@router.post("/create-tag")
async def create_tag(tag_req: Tag):
    logger.info(f"Creating tag {tag_req.name}")
    return await TagService.create_tag(tag_req)
    
@router.get("/get-tags")
async def get_tags():
    logger.info("Getting all tags")
    return await TagService.get_tags()

@router.post("/bind-tag")
async def bind_tag(binding_tag_req: BindingTag):
    logger.info(f"Binding tag {binding_tag_req.tag_name} to {binding_tag_req.agent_id}")
    return await TagService.bind_tag(binding_tag_req)
from fastapi import APIRouter, Request
from common.logger import logger
from ..model.tag import Tag
from ..model.banding_tag import BindingTag
from ..service.tag_service import TagService

router = APIRouter()

@router.post("/create-tag")
async def create_tag(tag_req: Tag, request: Request):
    logger.info(f"Creating tag {tag_req.name}")
    access_token = request.headers.get("Authorization")
    return await TagService.create_tag(tag_req, access_token)
    
@router.get("/get-tags")
async def get_tags(request: Request):
    logger.info("Getting all tags")
    access_token = request.headers.get("Authorization")
    return await TagService.get_tags(access_token)

@router.post("/bind-tag")
async def bind_tag(binding_tag_req: BindingTag, request: Request):
    logger.info(f"Binding tag {binding_tag_req.tag_ids} to {binding_tag_req.target_id}")
    access_token = request.headers.get("Authorization")
    return await TagService.bind_tag(binding_tag_req, access_token)
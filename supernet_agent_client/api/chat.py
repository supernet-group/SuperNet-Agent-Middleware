from fastapi import APIRouter,Request, HTTPException, status, Response
from fastapi.responses import StreamingResponse
from common.logger import logger
from ..model.chat import Chat
from ..service.chat_service import ChatService

router = APIRouter()

@router.post("/debug/chat")
async def debug_chat(chat:Chat, request: Request):
    logger.info("debug_chat")
    return await ChatService.debug_chat(chat, request.headers.get("Authorization"))


@router.get("/monitor")
async def monitor():
    pass
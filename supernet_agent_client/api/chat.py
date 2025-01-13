from fastapi import APIRouter,Request, HTTPException, status, Response
from fastapi.responses import JSONResponse
from common.logger import logger
from ..model.chat import Chat
from ..service.chat_service import ChatService

router = APIRouter()

@router.post("/chat")
async def debug_chat(chat:Chat, request: Request):
    return Response(await ChatService.debug_chat(chat, request.headers.get("Authorization")))
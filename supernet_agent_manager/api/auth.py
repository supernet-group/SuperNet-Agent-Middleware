from fastapi import APIRouter
from ..model.refresh_token import RefreshToken
from ..model.login import Login
from ..service.account_service import AccountService
from common.logger import logger

router = APIRouter()

# refresh token
@router.post("/refresh-token")
async def refresh_token(refresh_token_req: RefreshToken):
    logger.info("refresh_token_req: %s", refresh_token_req)
    result = await AccountService.refresh_token(refresh_token_req)
    return {"message": result}

# login (get access token and refresh token)
@router.post("/login")
async def login(login: Login):
    logger.info("login: %s", login)
    result = await AccountService.login(login)
    return {"message": result}


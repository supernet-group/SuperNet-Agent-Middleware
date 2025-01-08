from fastapi import APIRouter
from ..model.refresh_token import RefreshToken
from ..service.account_service import AccountService
from common.logger import logger

router = APIRouter()

@router.post("/refresh_token")
async def refresh_token(refresh_token_req: RefreshToken):
    logger.info("refresh_token_req: %s", refresh_token_req)
    result = AccountService.refresh_account_info(refresh_token_req)
    return {"message": result}

@router.get("/test_auth")
async def test_auth():
    return {"message": "test_auth"}
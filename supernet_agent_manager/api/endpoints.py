from fastapi import APIRouter
router = APIRouter()

@router.get("/ds")
async def do_something():
    result = "Something done!"
    return {"message": result}
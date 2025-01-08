import httpx
from ..model.generic_api_request import GenericAPIRequest
from fastapi import HTTPException

async def call(request: GenericAPIRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                params=request.params,
                data=request.data,
                json=request.json,
                timeout=10.0  # timeout
            )
            # check status code
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=str(e))
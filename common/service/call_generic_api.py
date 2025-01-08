import httpx
from ..model.generic_api_request import GenericAPIRequest
from fastapi import HTTPException
from common.logger import logger

async def call(request: GenericAPIRequest):
    logger.info(f"Calling {request.url} with method {request.method} and headers {request.headers} and params {request.params} and data {request.data} and json {request.json_data}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                params=request.params,
                data=request.data,
                json=request.json_data,
                timeout=10.0  # timeout
            )
            logger.info(f"Response status code: {response.status_code} and content: {response.content}")
            # check status code
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=str(e))
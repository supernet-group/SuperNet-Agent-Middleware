import httpx
import json
from ..model.generic_api_request import GenericAPIRequest
from fastapi import HTTPException
from fastapi.responses import JSONResponse
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
        error_response = {
            "status_code": e.response.status_code,
            "url": str(e.request.url),
            "method": e.request.method,
        }
        
        try:
            error_response["error"] = json.loads(e.response.content)
        except json.JSONDecodeError:
            error_response["error"] = {
                "message": e.response.content.decode("utf-8", errors="replace"),
                "raw_text": e.response.text
            }
        
        logger.error(f"HTTP request failed: {error_response}")
        
        return JSONResponse(
            content=error_response,
            status_code=e.response.status_code
        )
    except httpx.RequestError as e:
        error_response = {
            "status_code": 500,
            "error_type": e.__class__.__name__,
            "error_message": str(e),
            "url": str(getattr(e.request, 'url', 'Unknown')),
            "method": getattr(e.request, 'method', 'Unknown')
        }
        
        logger.error(f"Request failed: {error_response}")
        
        return JSONResponse(
            content=error_response,
            status_code=500
        )
    except Exception as e:
        error_response = {
            "status_code": 500,
            "error_type": "UnexpectedError",
            "error_message": str(e)
        }
        
        logger.exception("Unexpected error occurred")
        
        return JSONResponse(
            content=error_response,
            status_code=500
        )
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import logger
from app.core.exceptions import AppException


async def app_exception_handler(request: Request, exc: AppException):
    logger.warning(
        f"{request.method} {request.url.path} | "
        f"{exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )


async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"{request.method} {request.url.path} | Unexpected error: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "INTERNAL_ERROR",
                "message": "Unexpected error occurred"
            }
        }
    )
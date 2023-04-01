from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import traceback
import sys


class InternalServerErrorLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
        except Exception as exc:
            # Log the traceback of the error
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(
                exc_type, exc_value, exc_traceback, file=sys.stderr
            )

            # Respond with a 500 Internal Server Error
            response = JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )

        return response

from fastapi import FastAPI
from api.routes import router as api_router
from middlewares import InternalServerErrorLoggingMiddleware

app = FastAPI()
app.add_middleware(InternalServerErrorLoggingMiddleware)
app.include_router(
    api_router,
    prefix="/api",
    tags=["API"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal Server Error"},
    },
)


@app.get("/")
def root():
    return {"message": "Welcome to the YouTube Summary API!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI
import uvicorn

from app.api.routes import router
from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(router)


@app.on_event("startup")
async def startup():

    logger.info("===================================")
    logger.info("JARVIS STARTED")
    logger.info("===================================")


@app.on_event("shutdown")
async def shutdown():

    logger.info("Jarvis stopped.")


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
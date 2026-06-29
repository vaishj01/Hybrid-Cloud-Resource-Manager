from fastapi import FastAPI

from app.config.settings import settings

# Import engine
from app.database.database import engine

# Import Base
from app.models.base import Base
from app.models.user import User

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.on_event("startup")
def startup():

    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "Application": settings.APP_NAME,
        "Version": settings.APP_VERSION,
        "Status": "Running Successfully"
    }
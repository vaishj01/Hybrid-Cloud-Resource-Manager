from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.database.database import engine
from app.models.base import Base

from app.models.user import User
from app.models.resource import Resource

from app.routes.user_routes import router as user_router
from app.routes.resource_routes import router as resource_router
from app.routes.dashboard_routes import router as dashboard_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


app.include_router(user_router)
app.include_router(resource_router)
app.include_router(dashboard_router)
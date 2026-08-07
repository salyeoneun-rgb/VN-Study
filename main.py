from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="VN Study Journal",
    version="0.1.0"
)

# Static Files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# Templates
templates = Jinja2Templates(directory="app/templates")


from app.routers import home

app.include_router(home.router)


from app.database.database import engine
from app.database.base import Base

from app import models

Base.metadata.create_all(bind=engine)
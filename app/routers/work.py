from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from sqlalchemy.orm import Session

from app.crud import work as work_crud
from app.database.session import get_db

router = APIRouter(prefix="/works", tags=["Works"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def work_list(
    request: Request,
    db: Session = Depends(get_db),
):
    works = work_crud.get_all(db)

    return templates.TemplateResponse(
        request=request,
        name="works/index.html",
        context={
            "request": request,
            "works": works,
        },
    )


@router.post("/create")
async def create_work(
    title: str = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db),
):
    work_crud.create(
        db,
        title,
        description,
    )

    return RedirectResponse(
        "/works/",
        status_code=303,
    )
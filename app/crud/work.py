from sqlalchemy.orm import Session

from app.models.work import Work


def get_all(db: Session):
    return db.query(Work).order_by(Work.title).all()


def create(
    db: Session,
    title: str,
    description: str | None,
):
    work = Work(
        title=title,
        description=description,
    )

    db.add(work)
    db.commit()
    db.refresh(work)

    return work
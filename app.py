from fastapi import FastAPI, Depends, Request, Form, status
from prediction import make_prediction

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    all_news = db.query(models.News).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "news_list": all_news})


@app.post("/add")
async def add(request: Request, title: str = Form(...), text: str = Form(...), db: Session = Depends(get_db)):

    new_news = models.News(title=title, text=text, label=make_prediction(text))
    db.add(new_news)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{news_id}")
def delete(request: Request, news_id: int, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    db.delete(news)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

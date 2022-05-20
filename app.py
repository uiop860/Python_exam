from importlib.resources import path
from fastapi import FastAPI, Depends, Request, Form, status
from prediction import make_prediction
from wordclouds import word_cloud
from starlette.background import BackgroundTasks
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
import models
from database import SessionLocal, engine
import os
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/images",StaticFiles(directory="images"),name="images")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def remove_file(path: str) -> None:
    os.unlink(path)

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

@app.get("/generate/{news_id}")
async def generate (request: Request, news_id: int, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    news.path = word_cloud(news.id,news.text)
    db.add(news)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@app.get("/delete/{news_id}")
async def delete(background_tasks: BackgroundTasks ,request: Request, news_id: int, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    background_tasks.add_task(remove_file, f'./images/{news.path}')
    db.delete(news)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

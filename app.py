from typing import Optional

from fastapi import FastAPI, Request, Form, status, Depends

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

# import models
# from database import SessionLoca, engine

templates = Jinja2Templates(directory="templates")
# uvicorn app:app --reload
app = FastAPI()

#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db

#     finally:
#         db.close()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


def read_root():
    return {"Hello": "World"}


@app.post("/detect")
def detect_news(request: Request, title: str = Form(...), news: str = Form(...)):
    new_news = {"title": title, "news": news}
    return {"item_id": item_id, "q": q}

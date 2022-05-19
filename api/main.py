from typing import Optional

from fastapi import FastAPI, Request, Form, status, Depends

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

# import models
# from database import SessionLoca, engine

templates = Jinja2Templates(directory="../templates")

app = FastAPI()


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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

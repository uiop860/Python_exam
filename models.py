from sqlalchemy import Column, String, Integer

from database import Base


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    news = Column(String)
    label = Column(Integer)

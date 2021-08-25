from api_requests.news_request import NewsCreate
from datetime import datetime
from db.db_config import Base
# from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String
from sqlalchemy import Column
from sqlalchemy.orm import Session


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    slug = Column(String, nullable=False, index=True)
    isPublished = Column(Boolean, default=True)
    price = Column(Integer, nullable=False)
    createdAt = Column(DateTime, default=datetime.now())


def create_news(db: Session, news: NewsCreate):
    db_news = News(title=news.title, description=news.description,
                   slug=news.slug.replace(' ', "-").lower(), isPublished=news.isPublished, price=news.price)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

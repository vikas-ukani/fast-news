# from db.db_config import db_close, db_connection
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from api_requests.news_request import NewsCreate
from db.db_config import engine, get_db
from model import models

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

# EVENTS FOR
# Database Connection
# @app.on_event("startup")
# async def database_connect():
#     await db_connection()

# # Database Connection DROP
# @app.on_event("shutdown")
# async def database_disconnect():
#     await db_close()


@app.get('/')
def index():
    return {"message": "Welcome to FastAPI"}


@app.get('/news')
def news():
    return {"news": [], 'message': 'All news available here'}


@app.get('/news/{id}')
def getNews(id: int):
    return {
        'detail': {"id": id},
        'message': f"News Details available for id={id} news"
    }


@app.post('/news')
def create_news(request: NewsCreate, db: Session = Depends(get_db)):
    db_news = models.create_news(db=db, news=request)
    return {
        "data": db_news,
        "message": "News saved..."
    }

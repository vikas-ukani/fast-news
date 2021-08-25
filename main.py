from fastapi import FastAPI
from api_requests.news_request import NewsCreate

app = FastAPI()


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
def create_news(news: NewsCreate):
    return {
        "data": news,
        "message": "News saved..."
    }

from fastapi import FastAPI, Query
from pydantic import BaseModel
import wikipedia

app = FastAPI()

class ArticleRequest(BaseModel):
    title: str
    language: str

class ArticleResponse(BaseModel):
    title: str
    summary: str


# Path (Получить статью по названию)
@app.get("/article/{title}", response_model=ArticleResponse)
def article_path(title: str):
    summary = wikipedia.summary(title)
    return ArticleResponse(title=title, summary=summary)

# Query (Получить статью по названию и языку)
@app.get("/article", response_model=ArticleResponse)
def article_query(title: str, lang: str = "en"):
    wikipedia.set_lang(lang)
    summary = wikipedia.summary(title)
    return ArticleResponse(title=title, summary=summary)

# POST (Получить статью по названию и языку в теле JSON)
@app.post("/article", response_model=ArticleResponse)
def article_post(request: ArticleRequest):
    wikipedia.set_lang(request.language)
    summary = wikipedia.summary(request.title)
    return ArticleResponse(title=request.title, summary=summary)
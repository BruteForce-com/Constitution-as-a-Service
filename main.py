from http import HTTPStatus

from fastapi import FastAPI
from pydantic import BaseModel
from indianconstitution import IndianConstitution

app = FastAPI()
const = IndianConstitution()

class LoginRequest(BaseModel):
    username: str
    pwd: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/constitution/article/{article_number}")
def get_article(article_number: int):
    try:
        article = const.get_article(article_number)
        return {"article_number": article_number, "content": article}
    except Exception as e:
        return {"error": str(e)}, HTTPStatus.NOT_FOUND

@app.get("/constitution/part/{part_number}")
def get_part(part_number: int):
    try:
        part = const.get_part(part_number)
        return {"part_number": part_number, "content": part}
    except Exception as e:
        return {"error": str(e)}, HTTPStatus.NOT_FOUND

@app.get("/constitution/search/{keyword}")
def search_constitution(keyword: str):
    try:
        results = const.search(keyword)
        return {"keyword": keyword, "results": results}
    except Exception as e:
        return {"error": str(e)}, HTTPStatus.NOT_FOUND

@app.post("/login")
def login(request: LoginRequest):
    try:
        if request.username and request.pwd:
            return {"message": "success"}, HTTPStatus.OK
        return {"error": "Username and password required"}, HTTPStatus.BAD_REQUEST
    except Exception as e:
        return {"error": "Login failed"}, HTTPStatus.INTERNAL_SERVER_ERROR
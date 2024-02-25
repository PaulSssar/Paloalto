import re
from collections import Counter

from clickhouse_sqlalchemy import make_session
from db import Logs, engine
from fastapi import HTTPException, FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Domain(BaseModel):
    domain: str


@app.get('/categories/')
def get_categories():
    session = make_session(engine)
    categories = Counter(session.query(Logs.category).all())
    result = [{"category": key[0], "count": value} for key, value in categories.items()]
    return {"categories": result}


@app.get('/search/')
def search(domain: str = Query(...)):
    url_pattern = re.compile(r'^[A-Za-z0-9\-._~:/?#\[\]@!$&\'()*+,;=%]*$')
    if not url_pattern.match(domain):
        raise HTTPException(status_code=400, detail="Недопустимые символы в URL")
    session = make_session(engine)
    query = session.query(Logs).filter(Logs.url.ilike(f"%{domain}%"))
    result = [{
        "url": log.url,
        "category": log.category,
        "serial": log.serial,
        "receive_time": log.receive_time,
        "logs_time": log.logs_time
    } for log in query]
    return {"result": result}
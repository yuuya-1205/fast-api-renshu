from enum import Enum

# fastAPIをしようするためのimport
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# 決まった言葉だけ受け付ける
class Station(str, Enum):
    hello = "hello"
    codex = "codex"
    slack = "slack"


@app.get("/stations/{name}")
def read_station(name: Station):
    return {"station": name, "is_codex": name is Station.codex}

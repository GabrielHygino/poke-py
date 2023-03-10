from pymongo import MongoClient
from fastapi import FastAPI
from requests import get
from json import loads

app = FastAPI()
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["pokemon"]
collections = mydb["pokedex"]

@app.get("/pokelist")
def pokelist(var: str):
    for x in collections.find({"name":f"{var}"}):
        response = get(x["url"])
        formated_response = loads(response._content.decode())
    return (formated_response)

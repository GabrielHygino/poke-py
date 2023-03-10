from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()


myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["pokemon"]
collections = mydb["pokedex"]

var = "bulbasaur"

"""for x in collections.find({"name":f"{var}"}):
    print (x)"""


"""@app.get("/pokelist")
def pokelist():
    print(x)"""

@app.get("/pokelist")
def pokelist(var: str):
    for x in collections.find({"name":f"{var}"}):
        print (x)
    return {'Hello ' + var + '!'} 

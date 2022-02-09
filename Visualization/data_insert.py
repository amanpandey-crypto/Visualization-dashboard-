import pymongo
from pymongo import MongoClient
import json

client = pymongo.MongoClient('mongodb+srv://DecodeitAman:phychemmaths@cluster0.10xyo.mongodb.net/mydata?retryWrites=true&w=majority')
db = client["mydata"]
collection = db["mytable"]
requesting = []

with open("jsondata.json", encoding="utf8") as f:
    data=json.load(f)
    for jsonObj in data:
        requesting.append(jsonObj)

collection.insert_many(requesting)
print("finished")  
client.close()
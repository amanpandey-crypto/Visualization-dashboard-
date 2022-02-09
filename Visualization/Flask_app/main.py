from flask import Flask, jsonify, render_template
from flask_cors import CORS
from bson import json_util
import pymongo
import json


client = pymongo.MongoClient('mongodb+srv://DecodeitAman:phychemmaths@cluster0.10xyo.mongodb.net/mydata?retryWrites=true&w=majority')
db = client["mydata"]
collection = db["mytable"]

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/")
def index():
    data= getdata()
    # return jsonify(data)
    new_data = json.loads(json_util.dumps(data))
    return jsonify(new_data)


def getdata():
    data=collection.find()
    mylist=[]
    for i in data:
        mylist.append(i)    
    print(mylist)
    return mylist


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)


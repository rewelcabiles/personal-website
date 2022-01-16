from flask import Flask, render_template
from pymongo import MongoClient
import pymongo
import os

user_pass = os.environ.get("mongo_user") + ":" + os.environ.get("mongo_pass")
db_name = os.environ.get("mongo_db_name")
client = MongoClient("mongodb+srv://"+user_pass+"@prototype-cluster-0.jpk9n.mongodb.net/"+db_name+"?retryWrites=true&w=majority")
db = client[db_name]


app = Flask(__name__)

@app.route("/")
def index():
    featured_projects = db["projects"].find({"is_featured":True})
    other_projects = db["projects"].find({"is_featured":False})
    return render_template(
        "index.html",
        featured_projects=featured_projects,
        other_projects=other_projects)


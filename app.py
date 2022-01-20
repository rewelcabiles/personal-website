from flask import Flask, render_template
from pymongo import MongoClient
import pymongo
import os

db_uri = os.environ.get("db_uri")
client = MongoClient(db_uri)
db = client[os.environ.get("mongo_db_name")]


app = Flask(__name__)

@app.route("/")
def index():
    featured_projects = db["projects"].find({"is_featured":True}).sort("position")
    other_projects = db["projects"].find({"is_featured":False}).sort("position")
    return render_template(
        "index.html",
        featured_projects=featured_projects,
        other_projects=other_projects)


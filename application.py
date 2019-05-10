#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine("sqlite:///catalog.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/", methods=["GET"])
def mainPage():
    qCategories = session.query(Category).all()
    items = session.query(Item).all()
    qLastItems= []
    index = 0
    if items:
        while index < 10 and len(qLastItem) < len(items):
            qLastItems.append(items[index])
            index += 1
        return render_template("home.html", categories= qCategories, lastItems = qLastItems)
    else:
        return render_template("home.html")

# End of File #
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, threaded=False)

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
#create a Flask instance
app = app = Flask(__name__)


#connect to Mongo with PyMongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


#index route using Mongo data
@app.route("/")
def home():
    martian_data = mongo.db.collection.find_one()

    return render_template("index.html", marsfacts=martian_data)


#scrape route to trigger scrape function
@app.route("/scrape")

def scrape():

    mars_data = scrape_mars.scrape()

    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect("/")




if __name__ =="__main__":
    app.run(debug=True)
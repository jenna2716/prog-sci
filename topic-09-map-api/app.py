import json
from flask import Flask, render_template

app = Flask(__name__)
private = json.load(open("private.json","r"))

@app.route("/")
@app.route("/index")
def get_index():
    return render_template("index.html",api_key=private["API_KEY"], markers = [
    {
        "position": "37.4220656,-122.0840897",
        "title":"Mountain View, CA"
    },
    {
        "position": "47.648994,-122.3503845",
        "title":"Vancouver, BC",
        "label":{
            "text":"hello",
            "color":"white",
            "fontSize":"14px"
        }
    },
    {
        "position": "49.648994,-132.3503845",
        "title":"Somewhere, WA"
    }
    ])

@app.route("/map")
def get_map():
    return render_template("map.html", api_key=private["API_KEY"], settings = {"zoom":6, "center":{"lat":41.1513,"lng":-81.3578}}, markers = [{
        "position":{"lat":41.1513,"lng":-81.3578},
        "color":"4080FF",
        "scale":12,
        "label":{
            "text":"99",
            "color":"ffffff",
        }
    }])
        
if __name__ == "__main__":
    app.run(debug = True)
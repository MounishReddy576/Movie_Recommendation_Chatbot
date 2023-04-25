from flask import Flask, request, jsonify, render_template
import random
from backend import get_recommendations
from backend2 import get_movie_recommends
from genre import get_genre_recommendations

app = Flask(__name__, static_folder='static', template_folder='templates')

keywords = ['action', 'adventure', 'comedy', 'drama', 'romance', 'sci-fi', 'horror', 'animated', 'fantasy', 'thriller', 'crime', 'war', 'documentary']
intro_words = ['HI', 'hi', 'Hi', 'Hello', 'hello', 'help', 'Help', 'HELP']

# Function to generate a movie recommendation based on user input
def get_recommendation(message):
    if message in intro_words:
        return "Hi!, Please try movie name or genre to get recommendations."
    
    if message.lower() in keywords:
        rec = get_genre_recommendations(message).to_list()
        if len(rec) > 0:
            rec = "<br/>".join(rec)
            return "You might enjoy watching: <br/>" +  rec
        else:
            return "Sorry, I don't have any recommendations for " + message + " movies at the moment."
    else:
        rec = get_recommendations(message.title())
        if len(rec) > 0:
            rec = "<b>Recommender1: </b><br/>" + "<br/>".join(rec.to_list())
            return rec
        else:
            rec = get_movie_recommends(message.title())
            if len(rec) > 0:
                rec = "<b>Recommender2: </b><br/>" + "<br/>".join(rec.to_list())
                return rec
            else:
                return "Sorry, I don't have any recommendations for movies related to " + message + " at the moment."

@app.route("/")
def home():
    return render_template("index.html")

# Flask API endpoint to handle recommendation requests
@app.route("/recommendation")
def recommendation():
    message = request.args.get('message')
    recommendation = get_recommendation(message)
    response = {'message': recommendation}
    return jsonify(response)

if __name__ == "__main__":
    app.run()

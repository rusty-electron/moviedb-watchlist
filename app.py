from flask import Flask
from flask import render_template
from flask import request
from classes import search_movie, get_genre_dict, format_data

genre_dict = get_genre_dict()
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        search = request.form['search']
        movie_dict = search_movie(search)
        movie_dict = format_data(movie_dict, genre_dict)
        return render_template("index.html", movie_dict=movie_dict)
    else:
        return render_template("form.html")

if __name__ == "__main__":
    # run this part of code only when this script is run
    app.run(use_reloader=True, debug=True)

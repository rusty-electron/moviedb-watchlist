from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from .classes import search_movie, get_genre_dict, format_data

bp = Blueprint('search', __name__)

genre_dict = get_genre_dict()

@bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        search = request.form['search']
        movie_dict, _ = search_movie(search)
        movie_dict = format_data(movie_dict, genre_dict)
        return render_template("form.html", movie_dict=movie_dict)
    else:
        return render_template("form.html")

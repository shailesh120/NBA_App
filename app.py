from flask import *
from stats import *
from displays import *
from datetime import date
import requests

app = Flask(__name__)

def index():
    today = date.today()
    games, meta = get_all_games(today, page=1, per_page=30)

    players, meta = get_all_players(page = 1, per_page=9999)

    return render_template('index.html', games=games, players = players)

def search() -> str:
    today = date.today()
    games, meta = get_all_games(today, page=1, per_page=30)
    # Handle the search functionality here
    player_name = request.args.get('player_name')
    players = get_search_results(player_name.lower())
    return render_template('index.html', games = games, players=players, search_term=player_name)


app.add_url_rule('/', 'index', index)

app.add_url_rule('/search', 'search', search)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug=True)

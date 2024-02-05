from flask import *
from stats import *
from displays import *
from datetime import date
import requests

app = Flask(__name__)

def index():
    today = date.today()
    games, meta = get_all_games(today, page=1, per_page=30)
    return render_template('index.html', games=games)

app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    app.run(debug=True)
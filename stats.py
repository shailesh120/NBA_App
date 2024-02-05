import requests
from displays import *

def get_specific_player(player_id): # Specific Player
    base_url = f"https://www.balldontlie.io/api/v1/players/{player_id}"

    # Make API request to get player stats
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return None

def get_specific_team(team_id): # Specific Team
    base_url = f"https://www.balldontlie.io/api/v1/teams/{team_id}"

    # Make API request to get player stats
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return None


def get_all_players(page=1, per_page=25): # All players
    base_url = f"https://www.balldontlie.io/api/v1/players"
    params = {"page": page, "per_page": per_page}

    # Make API request to get player data
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        players = data.get("data", [])
        meta = data.get("meta", {})
        return players, meta
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return None, None

def get_all_teams(page=1, per_page=30): # All Teams
    base_url = f"https://www.balldontlie.io/api/v1/teams"
    params = {"page": page, "per_page": per_page}

    # Make API request to get player data
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        teams = data.get("data", [])
        meta = data.get("meta", {})
        return teams, meta
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return None, None

def get_season_avg(player_id, year): # Season Avg for one player
    base_url = f"https://www.balldontlie.io/api/v1/season_averages?season={year}&player_ids[]={player_id}"

    # Make API request to get player data
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        player_stats = data.get("data", [])
        return player_stats
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return None, None
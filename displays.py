def display_name(player):
    if player:
        print("-" * 30)
        print(f"Name: {player['first_name']} {player['last_name']}")
    else:
        print("No name available")

def display_player_info(player): # One player
    if player:
        print("-" * 30)
        print(f"Player ID: {player['id']}")
        print(f"Name: {player['first_name']} {player['last_name']}")
        print(f"Position: {player['position']}")
        print(f"Team: {player['team']['abbreviation']}")
        print("-" * 30)
    else:
        print("No player stats available.")

def display_team_info(team): # One team
    if team:
        print("-" * 30)
        print(f"Team Name: {team['full_name']}")
        print(f"Abb: {team['abbreviation']}")
        print(f"Conference: {team['conference']}")
        print(f"Division: {team['division']}")
        print("-" * 30)
    else:
        print("No team info available.")

def display_players_info(players): # All players
    if players:
        for player in players:
            print("-" * 30)
            print(f"Player ID: {player['id']}")
            print(f"Name: {player['first_name']} {player['last_name']}")
            print(f"Position: {player['position']}")
            print(f"Team: {player['team']['full_name']}")
        print("-" * 30)
    else:
        print("No player information available.")

def display_teams_info(teams): # All Teams
    if teams:
        for team in teams:
            print("-" * 30)
            print(f"Team Name: {team['full_name']}")
            print(f"Abb: {team['abbreviation']}")
            print(f"Conference: {team['conference']}")
            print(f"Division: {team['division']}")
        print("-" * 30)
    else:
        print("No team information available.")

def display_season_avg(player): # Season Avg
    if player:
        for i in player:
            print(f"{i['pts']} PPG")
            print(f"{i['ast']} APG")
            print(f"{i['reb']} RPG")
            print(f"{i['stl']} SPG")
            print(f"{i['blk']} BPG")
            print(f"{'{:.2f}'.format(i['fg_pct'] * 100)}% FG")
            print(f"{'{:.2f}'.format(i['fg3_pct'] * 100)}% 3PT")
            print(f"{'{:.2f}'.format(i['ft_pct'] * 100)}% FT")
        print("-" * 30)
    else:
        print("No team information available.")
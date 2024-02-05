from stats import *
from displays import *
from datetime import date


def main():
    again = "y"
    while again == "y":
        answer = input("What info would you like to get (enter number): \n1) Specific Player \n2) Specific Team \n3) All Players \n4) All Teams \n5) Player Season Avg \n6) Games on today \n \n")
        if answer == "1": # Specific Player
            player_id = int(input("Enter Player ID: "))  
            player = get_specific_player(player_id)
            display_player_info(player)
        elif answer == "3": # All Players
            page = 1
            per_page = int(input("How many players? \n")) 
            players, meta = get_all_players(page, per_page)
            display_players_info(players)
        elif answer == "4": # All Teams
            page = 1
            per_page = 30
            teams, meta = get_all_teams(page, per_page)
            display_teams_info(teams)
        elif answer == "2": # Specific Team
            team_id = int(input("Enter Team ID: ")) 
            team = get_specific_team(team_id)
            display_team_info(team)
        elif answer == "5": # Season Avg
            player_id = int(input("Enter Player ID: ")) 
            year = int(input("Enter Year: "))
            player = get_specific_player(player_id)
            display_name(player)
            player_stats = get_season_avg(player_id, year)
            display_season_avg(player_stats)
        elif answer == "6": # Season Avg
            today = date.today() 
            print(today)
            games, meta = get_all_games(today, page=1, per_page=30)
            display_all_games(games)        
        else:
            print("Not valid answer")
        again = input("Do you have another request? (y/n) \n")      
    

#----------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
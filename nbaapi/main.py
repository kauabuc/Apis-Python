
import requests

BASE_URL = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"


def get_scoreboard():
    scoreboard = requests.get(BASE_URL).json()['scoreboard']

    for game in scoreboard['games']:
        home_team = game['homeTeam']
        away_team = game['awayTeam']
        name_teamsHome = f"{home_team['teamCity']}  {home_team['teamName']}"
        name_teamAway = f"{away_team['teamCity']}  {away_team['teamName']}"
        victorysH = home_team["wins"]
        victorysA = away_team["wins"]
        print(f"{name_teamsHome} x {name_teamAway}")
        print(
            f'Contam com {victorysH} x {victorysA} de vitórias nessa temporada.')
        print()


get_scoreboard()

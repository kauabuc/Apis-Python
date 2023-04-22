from pprint import PrettyPrinter

import requests

BASE_URL = "http://data.nba.net/"
ALL_JSON = "prod/v1/today.json"
printer = PrettyPrinter()


def get_links():
    date = requests.get(BASE_URL + ALL_JSON).json()
    links = date['links']
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    response = requests.get(BASE_URL + scoreboard).json()['games']

    for game in response:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        print(f'{home_team['triCode']} x {away_team['triCode']}, {clock}, {period}')


get_scoreboard()

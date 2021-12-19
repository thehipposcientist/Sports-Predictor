from sportsipy.mlb.schedule import Schedule
from sportsipy.mlb.teams import Teams
import pandas as pd
from sportsipy.mlb.boxscore import Boxscores, Boxscore
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
import keras
import seaborn as sns

def get_curr_schedule():

    games_today = Boxscores(datetime.today())

    away = []
    home = []
    away_score = []
    home_score = []
    winner = []
    game_date = []

    for key in games_today.games.keys():
        away.extend(item['away_name'] for item in games_today.games[key])
        home.extend(item['home_name'] for item in games_today.games[key])
        away_score.extend(item['away_score'] for item in games_today.games[key])
        home_score.extend(item['home_score'] for item in games_today.games[key])
        winner.extend(item['winning_name'] for item in games_today.games[key])
        game_date.extend(item['boxscore'] for item in games_today.games[key])

    for i in range(len(game_date)):
        game_info = Boxscore(game_date[i])
        game_date[i] = game_info.date       


    return away, home, away_score, home_score, winner, game_date

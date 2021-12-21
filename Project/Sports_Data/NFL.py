from sportsipy.nfl.schedule import Schedule
from sportsipy.nfl.teams import Teams
import pandas as pd
from sportsipy.nfl.boxscore import Boxscores, Boxscore
from datetime import date
import requests
from bs4 import BeautifulSoup
import re
import keras
import seaborn as sns
import mysql.connector
from database import cursor

# function to get current week in the NFL
def get_current_week():
    # creating the date object of today's date
    todays_date = date.today()
    year = todays_date.year

    # web scrape CBS for current week
    url = 'https://www.cbssports.com/nfl/schedule/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="PageTitle-header").text
    try:
        current_week = int(re.search(r'\d+', results).group())
    except:
        print('Not in season')

    return current_week, year    

# function that retusn team nfl statistics
def get_nfl_team_stats():
    # This function collects NFL data and constructs 3 seperate NFL related dataframes
    teams = Teams()
    df = pd.DataFrame(columns = ['Name', 'Abbreviation', 'Penalties', 'Wins', 'Pass Attempts', 'Rush Attempts', 'First Downs',
                                'Turnovers', 'Strength of Schedule', 'Rushing Yards', 'Passing Yards', 'Fumbles', 'Interceptions'])

    # Get specific attributes from dictionary
    df['Name'] = [x.name for x in teams]
    df['Abbreviation'] = [x.abbreviation for x in teams]
    df['Wins'] = [x.wins for x in teams]
    df['Penalties'] = [x.penalties for x in teams]
    df['Pass Attempts'] = [x.pass_attempts for x in teams]
    df['Rush Attempts'] = [x.rush_attempts for x in teams]
    df['First Downs'] = [x.first_downs for x in teams]
    df['Turnovers'] = [x.turnovers for x in teams]
    df['Strength of Schedule'] = [x.strength_of_schedule for x in teams]
    df['Rushing Yards'] = [x.rush_yards for x in teams]
    df['Passing Yards'] = [x.pass_yards for x in teams]
    df['Fumbles'] = [x.fumbles for x in teams]
    df['Interceptions'] = [x.interceptions for x in teams]

# function that returns this week schedule in a list of lists
def get_curr_sched():

    current_week, year = get_current_week()
    away = []
    home = []
    away_score = []
    home_score = []
    winner = []
    game_date = []

    games_today = Boxscores(current_week, year)
    # Prints a dictionary of all matchups for current week of current year

    # Construct this weeks schedule array
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

# function that returns history of games in a list of lists
def get_history_of_seasons():
    # Construct a dataframe containing the last 5 years of games
    history_of_seasons = pd.DataFrame(columns = ['Away Team', 'Home Team', 'Away Score', 'Home Score', 'Winner'])

    week, year = get_current_week()
    week = week-1
    away = []
    home = []
    away_score = []
    home_score = []
    winner = []
    curr_year = year

    while curr_year >= year-5:
        if curr_year != year: week = 16
        while week >= 1:
            previous_games = Boxscores(week, curr_year)
            for key in previous_games.games.keys():
                away.extend(item['away_name'] for item in previous_games.games[key])
                home.extend(item['home_name'] for item in previous_games.games[key])
                away_score.extend(item['away_score'] for item in previous_games.games[key])
                home_score.extend(item['home_score'] for item in previous_games.games[key])
                winner.extend(item['winning_name'] for item in previous_games.games[key])
            week = week-1 
        curr_year = curr_year-1

    history = [away, home, away_score, home_score, winner]

    return history

def prediction():
    pass
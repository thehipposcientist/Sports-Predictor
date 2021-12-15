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


def get_current_week():
    # creating the date object of today's date
    todays_date = date.today()

    # web scrape CBS for current week
    url = 'https://www.cbssports.com/nfl/schedule/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="PageTitle-header").text
    try:
        current_week = int(re.search(r'\d+', results).group())
    except:
        print('Not in season')

    return current_week, todays_date    

def collect_nfl_information():
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

def get_current_schedule():

    current_week,todays_date = get_current_week()
    year = todays_date.year

    games_today = Boxscores(current_week, todays_date.year)
    # Prints a dictionary of all matchups for current week of current year

    current_schedule = pd.DataFrame(columns = ['Away Team', 'Home Team', 'Away Score', 'Home Score', 'Winner'])

    # Construct this weeks schedule dataframe
    for key in games_today.games.keys():
        current_schedule['Away Team'] =  [item['away_name'] for item in games_today.games[key]]
        current_schedule['Home Team'] =  [item['home_name'] for item in games_today.games[key]]
        current_schedule['Away Score'] =  [item['away_score'] for item in games_today.games[key]]
        current_schedule['Home Score'] =  [item['home_score'] for item in games_today.games[key]]
        current_schedule['Winner'] =  [item['winning_name'] for item in games_today.games[key]]

    return current_schedule

def get_history_of_seasons():
    # Construct a dataframe containing the last 5 years of games
    history_of_seasons = pd.DataFrame(columns = ['Away Team', 'Home Team', 'Away Score', 'Home Score', 'Winner'])


    week,todays_date = get_current_week()
    year = todays_date.year
    away = []
    home = []
    away_score = []
    home_score = []
    winner = []

    while year >= todays_date.year-5:
        if year != todays_date.year: week = 16
        while week >= 1:
            previous_games = Boxscores(week, year)
            for key in previous_games.games.keys():
                away.extend(item['away_name'] for item in previous_games.games[key])
                home.extend(item['home_name'] for item in previous_games.games[key])
                away_score.extend(item['away_score'] for item in previous_games.games[key])
                home_score.extend(item['home_score'] for item in previous_games.games[key])
                winner.extend(item['winning_name'] for item in previous_games.games[key])
            week = week-1 
        year = year-1

    history_of_seasons['Away Team'] =  away
    history_of_seasons['Home Team'] =  home
    history_of_seasons['Away Score'] = away_score
    history_of_seasons['Home Score'] =  home_score
    history_of_seasons['Winner'] =  winner

    # Match today's names with the previous ones to help machine learning algorithm
    history_of_seasons=history_of_seasons.replace({'Oakland Raiders': 'Las Vegas Raiders', 'St. Louis Rams':'Los Angeles Rams',
                        'Washington Redskins':'Washington Football Team'}, regex=True)    

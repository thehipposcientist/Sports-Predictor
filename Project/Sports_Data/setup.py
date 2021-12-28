import mysql.connector
from database import cursor, db

DB_NAME = 'Sports'

TABLES = {}

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

create_database()    

# Not created yet
TABLES['nfl'] = "CREATE TABLE nfl ( id INTEGER(11) AUTO_INCREMENT PRIMARY KEY, home_team VARCHAR(50) NOT NULL, away_team VARCHAR(50) NOT NULL, home_score INT(3) NOT NULL, away_score INT(3) NOT NULL, winner VARCHAR(50) NOT NULL, week int(2) NOT NULL, season int(5) NOT NULL);"

def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    cursor.execute(TABLES['nfl'])

create_tables()

def add_nfl(home, away, home_score, away_score, winner, week, season):
    sql = ("INSERT INTO nfl(home, away, home_score, away_score, winner, week, season) VALUES (%s, %s, %i, %i, %s, %i, %i)")
    cursor.execute(sql, (home, away, home_score, away_score, winner, week, season))
    db.commit()
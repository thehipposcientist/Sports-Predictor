import mysql.connector
from database import cursor

DB_NAME = 'Sports'

TABLES = {}

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

create_database()    

TABLES['nfl'] = (
    "CREATE TABLE 'nfl' ("
     "'id' int(11) NOT NULL"
     " 'home_team' varchar(50) NOT NULL AUTO_INCREMENT,"
     " 'away_team' varchar (50) NOT NULL,"
     " 'home_score' int(3) NOT NULL,"
     " 'away_score' int(3) NOT NULL,"
     " 'week' int(2) NOT NULL,"
     " 'season' int(5) NOT NULL,"
     " PRIMARY KEY ('id')"
     ") ENGINE=InnoDB"
)
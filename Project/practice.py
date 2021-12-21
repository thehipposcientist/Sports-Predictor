import mysql.connector

db = mysql.connector.connect()

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Turtle94',
    database = 'testdatabase'
)

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Person (name VARCHAR(100), age smallint, personID int PRIMARY KEY AUTO_INCREMENT)")

print(mycursor.execute("DESCRIBE person"))
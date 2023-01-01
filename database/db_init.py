import mysql.connector as DatabaseConnector
from dotenv import load_dotenv
import os


load_dotenv()
# MYSQL DATABASE CONNECTION
databaseLocalhostPassword = os.getenv("databaseLocalhostPassword")

try:
    db = DatabaseConnector.connect(
    host = 'localhost',
    user = 'BetterMoney', 
    passwd = databaseLocalhostPassword, 
    database = 'BetterMoney')
    print("Successfully Connected to MySQL Database")
    dbCursor = db.cursor()
except:
    print("Something is Wrong with MySQL Connection!")


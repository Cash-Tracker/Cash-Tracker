import mysql.connector as DatabaseConnector
from dotenv import load_dotenv
import os


load_dotenv()
# MYSQL DATABASE CONNECTION
try:
    db = DatabaseConnector.connect(
    host = os.getenv("dbhost"),
    user = os.getenv("dbusername"), 
    passwd = os.getenv("dbpassword"), 
    database = os.getenv("database"),
    )
    print("Successfully Connected to MySQL Database")
    dbCursor = db.cursor()
except:
    print("Something is Wrong with MySQL Connection!")
from database.db_init import dbCursor, db



def getSummary(year, month, ID) -> list:
    query = "SELECT amount, category FROM spent WHERE strftime('%m', datetime) = ? AND strftime('%Y', datetime) = ? AND userID = ?"
    dbCursor.execute(query, (month, year, ID))
    return dbCursor.fetchall()

def pushSpent(ID, amount, category, onWhat, note, datetime) -> None:
    query = "INSERT INTO spent VALUES (?, ?, ?, ?, ?, ?)"
    dbCursor.execute(query, (ID, amount, category, onWhat, note, datetime))
    db.commit()


# pushSpent(2, 200, 'food', 'BunSamosax2', 'IDK', "2022-12-15 20:00:00")
# print(getSummary("2022", "12", 2))



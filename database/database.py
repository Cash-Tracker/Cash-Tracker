from database.db_init import dbCursor, db



# dbCursor.execute("SELECT * FROM testTable;")

# print(dbCursor.fetchall())


def getSummary(year, month, ID) -> list:
    dbCursor.execute(f"select amount, category from spent where month(datetime) = {month} and year(datetime) = {year} and userID = '{ID}'")
    return dbCursor.fetchall()


def pushSpent(ID, amount, category, onWhat, note, datetime) -> None: 
    dbCursor.execute(f"insert into spent values('{ID}', {amount}, '{category}', '{onWhat}', '{note}', '{datetime}')")
    db.commit()


# pushSpent(2, 200, 'food', 'BunSamosax2', 'IDK', "2022-12-15 20:00:00")




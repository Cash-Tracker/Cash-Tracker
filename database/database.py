from database.db_init import dbCursor, db



def getSummary(year, month, ID) -> list:
    dbCursor.execute(f"select amount, category from spent where month(datetime) = {} and year(datetime) = {} and userID = '{}'".format{month,year,ID})
    return dbCursor.fetchall()


def pushSpent(ID, amount, category, onWhat, note, datetime) -> None: 
    dbCursor.execute(f"insert into spent values('{}', {}, '{}', '{}', '{}', '{}')".format{ID, amount, category, onWhat, note, datetime})
    db.commit()


# pushSpent(2, 200, 'food', 'BunSamosax2', 'IDK', "2022-12-15 20:00:00")
# print(getSummary("2022", "12", 2))



from database.db_init import dbCursor, db


def getSummary(year, month, ID) -> list:
    dbCursor.execute(
        "SELECT amount, category FROM spent WHERE month(datetime) = %(month)s and year(datetime) = %(year)s and userID = %(ID)s",
        {"month": month, "year": year, "ID": ID},
    )
    return dbCursor.fetchall()


def pushSpent(ID, amount, category, onWhat, note, datetime) -> None:
    dbCursor.execute(
        "INSERT INTO spent VALUES(%(ID)s, %(amount)s, %(category)s, %(onWhat)s, %(note)s, %(datetime)s)",
        {
            "ID": ID,
            "amount": amount,
            "category": category,
            "onWhat": onWhat,
            "note": note,
            "datetime": datetime,
        },
    )
    db.commit()


# pushSpent(2, 200, 'food', 'BunSamosax2', 'IDK', "2022-12-15 20:00:00")
# print(getSummary("2022", "12", 2))

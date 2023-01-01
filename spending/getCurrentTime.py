import datetime

# SIRI
# YYYY-MM-DD HH:MM:SS
def getCurrentTime() -> str:
    now = datetime.datetime.now()
    formattedDateTime = now.strftime(r"%Y-%m-%d %H:%M:%S")
    return formattedDateTime


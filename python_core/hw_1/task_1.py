import datetime
import re

def get_days_from_today(date:str):
    now_day = datetime.datetime.today()
    correct_input_date = re.sub("[^0-9]", "-", date)
    diference_of_date = now_day - datetime.datetime.strptime(correct_input_date, "%Y-%m-%d")
    return(diference_of_date.days)

print(get_days_from_today("2122.12=15"))
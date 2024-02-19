from datetime import datetime, timedelta

def get_upcoming_birthdays(users:list) -> list:
    now_date = datetime.today().date()
    congratulations_list = []
    for user in users:
        birthday_date = datetime.strptime(user["birthday"],"%Y.%m.%d").date()

        birthday_date_this_year = datetime.strptime(f"{now_date.year}-{birthday_date.month}-{birthday_date.day}","%Y-%m-%d").date()

        if birthday_date_this_year < now_date:
            birthday_date_this_year += timedelta(days=birthday_date_this_year.day + 1)

        days_to_birthday = (birthday_date_this_year - now_date).days


        if 0 <= days_to_birthday <= 7:
            if birthday_date_this_year.weekday() >= 5:
                days_to_birthday += 7 - birthday_date_this_year.weekday()
            
            congratulation_date = now_date + timedelta(days=days_to_birthday)
            final_congratulation_date = datetime.strftime(congratulation_date, "%Y.%m.%d")

            congratulations_list.append({
                "name" : user["name"],
                "congratulation_date" : final_congratulation_date
            })

    return congratulations_list
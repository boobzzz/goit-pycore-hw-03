from typing import List, Dict
from datetime import datetime

users_list = [
    {"name": "John Doe", "birthday": "1985.07.07"},
    {"name": "Jane Smith", "birthday": "1990.09.18"},
    {"name": "Alex Longhorn", "birthday": "1982.07.16"},
    {"name": "Barbara Jackson", "birthday": "1995.07.15"},
    {"name": "Anthony McBright", "birthday": "1990.08.13"},
    {"name": "Isaac Clark", "birthday": "1998.07.12"},
    {"name": "Jack White", "birthday": "1990.07.01"},
    {"name": "Joan Davis", "birthday": "1990.07.13"}
]


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    today = datetime.today().date()
    bd_data_list = []

    for user in users:
        user_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if user_date.month == today.month and today.day <= user_date.day <= today.day + 7:
            user_bd_data = {
                "name": user["name"],
                "congratulation_date": get_congratulation_date(user_date)
            }
            bd_data_list.append(user_bd_data)
        bd_data_list.sort(key=get_day)

    return bd_data_list


def get_congratulation_date(user_date) -> str:
    today = datetime.today().date()
    day = user_date.day
    c_date = datetime(today.year, today.month, day)
    if c_date.weekday() == 5:
        day += 2
    if c_date.weekday() == 6:
        day += 1

    return f"{today.year}.{today.month}.{day}"


def get_day(element):
    return datetime.strptime(element["congratulation_date"], "%Y.%m.%d").date().day


get_upcoming_birthdays(users_list)

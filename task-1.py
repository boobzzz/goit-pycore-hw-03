from datetime import datetime


def get_days_from_today(date: str) -> int:
    date_today = datetime.today()
    new_date = date_today
    delta_days = 0

    try:
        new_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print('Please make sure the entered date format is valid: YYYY-MM-DD')
        return delta_days

    delta_days = (new_date - date_today).days
    return delta_days

from excel_manager import create_user_excel, update_daily_data

def login_user(user_id):
    create_user_excel(user_id)
    return True

def add_calories(user_id, value):
    update_daily_data(user_id, calories=value)

def add_water(user_id, value=250):
    update_daily_data(user_id, water=value)

def rate_day(user_id, rating):
    update_daily_data(user_id, rating=rating)

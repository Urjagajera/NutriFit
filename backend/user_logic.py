from excel_manager import (
    create_user,
    save_quiz,
    create_user_file,
    update_daily_data,
    get_user_by_credentials,
    get_user_by_id
)
from session_manager import login, current_user


# ---------- AUTH ----------

def register_user(email, password):
    user_id = create_user(email, password)
    login(user_id)
    create_user_file(user_id)
    return user_id


def login_user(email, password):
    user = get_user_by_credentials(email, password)
    if not user:
        return False
    login(user["user_id"])
    return True


# ---------- PROFILE / QUIZ ----------

def save_user_quiz(form_data):
    user_id = current_user()
    if not user_id:
        return False

    quiz_data = {
        "age": form_data["age"],
        "gender": form_data["gender"],
        "height": form_data["height"],
        "weight": form_data["weight"],
        "food": form_data.get("food_habit", ""),
        "sleep": form_data.get("sleep", ""),
        "medical": form_data.get("medical", "")
    }

    save_quiz(user_id, quiz_data)
    return True


def get_user_profile():
    user_id = current_user()
    if not user_id:
        return None
    return get_user_by_id(user_id)


# ---------- DAILY TRACKING ----------

def add_calories(value):
    user_id = current_user()
    update_daily_data(user_id, calories=value)


def add_water():
    user_id = current_user()
    update_daily_data(user_id, water=250)


def rate_day(rating):
    user_id = current_user()
    update_daily_data(user_id, rating=rating)

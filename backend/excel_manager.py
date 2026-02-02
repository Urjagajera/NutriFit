import pandas as pd
import os
from datetime import date

DATA_DIR = "backend/data"
USERS_FILE = os.path.join(DATA_DIR, "users.xlsx")

os.makedirs(DATA_DIR, exist_ok=True)

def init_users_file():
    if not os.path.exists(USERS_FILE):
        df = pd.DataFrame(columns=[
            "user_id", "email", "password", "focus",
            "age", "gender", "height", "weight",
            "food", "sleep", "medical"
        ])
        df.to_excel(USERS_FILE, index=False)

def create_user(email, password):
    init_users_file()
    df = pd.read_excel(USERS_FILE)
    user_id = len(df) + 1
    df.loc[len(df)] = [user_id, email, password, "", "", "", "", "", "", "", ""]
    df.to_excel(USERS_FILE, index=False)
    create_user_file(user_id)
    return user_id

def create_user_file(user_id):
    path = os.path.join(DATA_DIR, f"user_{user_id}.xlsx")
    if not os.path.exists(path):
        pd.DataFrame(columns=["date", "calories", "water", "rating"]).to_excel(path, index=False)

def save_quiz(user_id, data):
    df = pd.read_excel(USERS_FILE)
    idx = df[df["user_id"] == user_id].index[0]

    for key in data:
        df.loc[idx, key] = data[key]

    df.to_excel(USERS_FILE, index=False)

def get_all_users():
    init_users_file()
    return pd.read_excel(USERS_FILE)

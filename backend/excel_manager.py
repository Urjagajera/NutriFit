import pandas as pd
import os
from datetime import date

DATA_DIR = "backend/data"

def get_user_file(user_id):
    return os.path.join(DATA_DIR, f"user_{user_id}.xlsx")


def create_user_excel(user_id):
    path = get_user_file(user_id)
    if not os.path.exists(path):
        df = pd.DataFrame(columns=["date", "calories", "water_ml", "rating"])
        df.to_excel(path, index=False)


def update_daily_data(user_id, calories=0, water=0, rating=None):
    path = get_user_file(user_id)
    today = str(date.today())

    df = pd.read_excel(path)

    if today in df["date"].values:
        idx = df[df["date"] == today].index[0]
        df.loc[idx, "calories"] += calories
        df.loc[idx, "water_ml"] += water
        if rating:
            df.loc[idx, "rating"] = rating
    else:
        df.loc[len(df)] = [today, calories, water, rating]

    df.to_excel(path, index=False)

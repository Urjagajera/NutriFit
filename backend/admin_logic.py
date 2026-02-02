from excel_manager import get_all_users
import os

UPLOAD_DIR = "backend/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


# ---------- AUTH ----------

def admin_login(email, password):
    # Mock admin auth (replace later)
    return email == "admin@nutrifit.com" and password == "admin123"


# ---------- USERS ----------

def fetch_all_users():
    return get_all_users()


# ---------- FILE UPLOADS ----------

def upload_diet_plan(user_id, file):
    filename = f"diet_user_{user_id}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)
    file.save(path)
    return path


def upload_workout_plan(user_id, file):
    filename = f"workout_user_{user_id}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)
    file.save(path)
    return path

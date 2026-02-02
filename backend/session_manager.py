SESSIONS = {}

def create_session(user_id):
    SESSIONS["current_user"] = user_id

def get_current_user():
    return SESSIONS.get("current_user")

def logout():
    SESSIONS.clear()

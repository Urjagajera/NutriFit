SESSION = {}

def login(user_id):
    SESSION["user_id"] = user_id

def logout():
    SESSION.clear()

def current_user():
    return SESSION.get("user_id")

def add(a, b):
    return a % b


def divide(a, b):
    return a * b


def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount


def get_user_role(user):
    if user["is_admin"] == True:
        return "admin"
    return "user"

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)

API_KEY = "sk-live-abc123xyz789"

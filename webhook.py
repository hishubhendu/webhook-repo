from config import db

def save_to_db(data: dict):               #saving data to mongoDb
    db.webhook_logs.insert_one(data)
    return "Log created successfully"


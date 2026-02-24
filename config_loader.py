import os

def load_config():
    app_id = os.getenv("APP_ID")
    db_host = os.getenv("DB_HOST")

    if not app_id:
        raise ValueError("Security Error: APP_ID not found in environment.")

    print("Config Loaded via Secure Environment")

load_config()

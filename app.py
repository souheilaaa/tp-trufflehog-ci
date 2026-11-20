import os

DATABASE_URL = os.getenv("DATABASE_URL")

def notify():
    print("Sending alert...")

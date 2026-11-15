import json
import os

DATA_FILE = "users.json"


def create_default_data():
    data = {
        "atm_cash": 5000.00,
        "users": {
            "user01": {
                "name": "user01",
                "password": "Test@123",
                "account_number": "10010001",
                "balance": 2500.00,
                "card_status": "active",
                "failed_attempts": 0,
                "lockout_until": None,
                "last_login": None,
                "deposited_today": 0.0,
                "withdrawn_today": 0.0,
                "transfers_today": 0,
                "last_reset_date": None,
                "history": [],
                "last_transaction": None
            },
            "user02": {
                "name": "user02",
                "password": "Test@456",
                "account_number": "10010002",
                "balance": 1500.00,
                "card_status": "active",
                "failed_attempts": 0,
                "lockout_until": None,
                "last_login": None,
                "deposited_today": 0.0,
                "withdrawn_today": 0.0,
                "transfers_today": 0,
                "last_reset_date": None,
                "history": [],
                "last_transaction": None
            },
            "user03": {
                "name": "user03",
                "password": "Test@789",
                "account_number": "10010003",
                "balance": 3000.00,
                "card_status": "active",
                "failed_attempts": 0,
                "lockout_until": None,
                "last_login": None,
                "deposited_today": 0.0,
                "withdrawn_today": 0.0,
                "transfers_today": 0,
                "last_reset_date": None,
                "history": [],
                "last_transaction": None
            }
        }
    }
    return data


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data():
    if not os.path.exists(DATA_FILE):
        data = create_default_data()
        save_data(data)
        return data

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Xəta: məlumat faylı zədəlidir. Başlanğıc məlumatlar yenidən yaradılır.")
        data = create_default_data()
        save_data(data)
        return data
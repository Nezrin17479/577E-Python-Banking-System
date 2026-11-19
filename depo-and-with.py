from storage import *
from datetime import datetime as dt


data = load_data()
# print(data['users']['user01']['password'])

def balance(username):
    info=data['users'][username]
    print(f"Account Holder: {info['name']}")
    print(f"Account Number: {info['account_number']}")
    print(f"Available Balance: {info['balance']}")
    print(f"Account Status: {info['card_status']}")


def deposit():
    pass
    
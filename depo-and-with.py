from storage import *
from datetime import datetime as dt


data = load_data()
max_depo=2000.0
# print(data['users']['user01']['password'])

def balance(username):
    info=data['users'][username]
    print(f"Account Holder: {info['name']}")
    print(f"Account Number: {info['account_number']}")
    print(f"Available Balance: {info['balance']}")
    print(f"Account Status: {info['card_status']}")


def deposit(username, depo_amount):
    info=data['users'][username]
    depo_today=info['deposited_today']
    time_check=dt.now().strftime('%X')
    print(f'Deposited today: {depo_today}', end='\n')
    print(f'Requested deposit: {depo_amount}', end='\n')
    print('Daily deposit maximum: 2000.0', end='\n')
    print(f'Remaining deposit allowance: {max_depo - depo_today}')

    
    if info['last_reset_date'] != time_check:
        data['users'][username]['last_reset_date']=time_check
        data['users'][username]['deposited_today']=0.0

    if depo_amount < 0:
        return 'Deposit amount must be positive'

    elif depo_amount + depo_today > max_depo:
        print('Deposit declined: daily limit would be exceeded', end='\n')
        print('Account balance and ATM cash remain unchanged.')
        return

    else:
        data['atm_cash'] += depo_amount
        data['users'][username]['balance'] += depo_amount
    
    return 

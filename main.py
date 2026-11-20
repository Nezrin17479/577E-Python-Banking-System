from auth import check_login, failed_attempts, password_changing

from storage import load_data, save_data
from datetime import datetime, timedelta

def show_start_menu():
    print("\n=== PYTHON BANKING SYSTEM ===")
    print("1. Login")
    print("2. Sign up")
    print("0. Exit")


def show_main_menu(username):
    print("\n=== PYTHON BANKING SYSTEM ===")
    print(f"Welcome, {username}!")
    print("1. View account information")
    print("2. Check balance")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Transfer money")
    print("6. Transaction history")
    print("7. Daily limits")
    print("8. Change password")
    print("9. Logout")
    print("0. Exit")


def main_menu_loop(data, username):
    while True:
        show_main_menu(username)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_info = data['users'][username]
            print("\n--- ACCOUNT INFORMATION ---")
            for key, value in user_info.items():
                print(f"{key}: {value}")
            print("---------------------------")
            input("Press Enter to continue...")
        elif choice == "2":
            information=balance(data,username)
        elif choice == "3":
            deposit_money=deposit()
        elif choice == "4":
            withdraw_money=withdraw()
        elif choice == "5":
            transfer_money=transfer()
        elif choice == "6":
            transaction_money=transaction()
        elif choice == "7":
            daily_limits_money=daily_limits()
        elif choice == "8":
            
            while True:
                res=password_changing(data,username)
                if res=='True':
                    print("Password successfully changed!")
                    break
                else:
                    
                    continue

        elif choice == "9":
            print("You have been logged out.")
            return True
        elif choice == "0":
            print("Goodbye!")
            return False
        else:
            print("Invalid choice. Please enter a number from the menu.")


def main():
    data = load_data()

    while True:
        show_start_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password=input("Password: ").strip()
            now=datetime.now()
            acces=check_login(now,data, username, password)
            
            if acces=='True':
                main_menu_loop(data, username)
            elif acces=='2':
                print('Wrong username or password')

            elif acces=='False':
                if failed_attempts(now,data, username)==True:
                    main()
                elif failed_attempts(now,data, username)==False:
                    print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
                else:
                    print('Wrong username or password')
                    main()
                    
        elif choice == "2":
            new_user = input("Username: ").strip()
            
            if new_user in data['users']:
                print("Username already exists! Please choose another one.")
                continue
                
            new_password = input("Password: ").strip()
            
 
            if len(new_password) < 8:
                print("Password must be at least 8 characters long.")
                continue
            if not any(c.isupper() for c in new_password):
                print("Password must contain at least one uppercase letter.")
                continue
            if not any(c.islower() for c in new_password):
                print("Password must contain at least one lowercase letter.")
                continue
            if not any(c.isdigit() for c in new_password):
                print("Password must contain at least one digit.")
                continue

            k = len(data['users'])
            

            
            data["users"][new_user] = {
                "name": new_user,
                "password": new_password,
                "account_number": "1001000" + str(k + 1),
                "balance": 0.0,
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
            
            save_data(data)
            print("Sign up successful! You can now log in.")

if __name__ == "__main__":
    main()



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
            print("Account information - coming soon")
        elif choice == "2":
            print("Check balance - coming soon")
        elif choice == "3":
            print("Deposit - coming soon")
        elif choice == "4":
            print("Withdraw - coming soon")
        elif choice == "5":
            print("Transfer - coming soon")
        elif choice == "6":
            print("Transaction history - coming soon")
        elif choice == "7":
            print("Daily limits - coming soon")
        elif choice == "8":
            print("Change password - coming soon")
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
            
            if acces==True:
                main_menu_loop(data, username)
            elif access==2:
                print('Wrong username or password')
            else:
                if failed_attempts(now,data, username)==True:
                    main()
                elif failed_attempts(now,data, username)==False:
                    print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
                else:
                    print('Wrong username or password')
                    main()
                    
        elif choice == "2":
            new_user=input("Username: ").strip()
            new_password=input("Password: ").strip()
            k=len(data['users'])
            data_user='user0'+str(k+1)
            data["users"][data_user] = {
                "name": new_user,
                "password": new_password,
                "account_number": "1001000"+str(k+1),
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

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()


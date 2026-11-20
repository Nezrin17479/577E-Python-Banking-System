import hashlib
import time
from datetime import datetime, timedelta
from storage import load_data, save_data


def blocked_user(seconds=60):
    print("Too many failed login attempts.")
    for remaining_time in range(seconds, -1, -1):
        print(f"\rPlease wait: 00:{remaining_time:02d} ", end="")
        time.sleep(1)
    print("\nYou may try again.\n")
    return 1

def check_login(now, data, username, password):
    if username in data["users"]:
        lockout_str = data["users"][username]["lockout_until"]
        if lockout_str is not None and lockout_str != 'None':
            lockout_time = datetime.strptime(lockout_str, "%Y-%m-%d %H:%M:%S")
            if now < lockout_time:
                left_second = int((lockout_time - now).total_seconds())
                blocked_user(left_second)
                return '5'
            else:
                data["users"][username]["lockout_until"] = None
                save_data(data)

        if data["users"][username]["card_status"] == 'active':
            main_password = data["users"][username]["password"]
            hash_object_user = hashlib.sha256(main_password.encode('utf-8'))
            hashed_result_user = hash_object_user.hexdigest()

            accessed_password = hashlib.sha256(password.encode('utf-8'))
            accessed_password_result = accessed_password.hexdigest()
            if hashed_result_user == accessed_password_result:
                data["users"][username]["failed_attempts"] = 0
                data['users'][username]['last_login'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                save_data(data) 
                return 'True'
            else:
                data["users"][username]["failed_attempts"] += 1
                save_data(data) 
                return 'False'
        else:
            print('Maximum login attempts exceeded. Your card has been blocked. Please contact the bank administrator.')
            return '5'
    else:
        return '2'

def failed_attempts(now, data, username):
    if data["users"][username]["failed_attempts"] == 3 or data["users"][username]["failed_attempts"] == 6:
        if data["users"][username]["failed_attempts"] == 3:
            blocked_user(seconds=60)
            data["users"][username]["lockout_until"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        else:
            data["users"][username]["card_status"] = 'blocked'
            save_data(data) 
            return False

def password_changing(data, username):
    password = input('Enter your current password: ').strip()
    if password == data['users'][username]['password']:
        new_password = input('Please enter your new password: ')
        if len(new_password) < 8:
            print("Password must be at least 8 characters long.")
            return 'False'
               
        if not any(c.isupper() for c in new_password):
            print("Password must contain at least one uppercase letter.")
            return 'False'
             
        if not any(c.islower() for c in new_password):
            print("Password must contain at least one lowercase letter.")
            return 'False'
              
        if not any(c.isdigit() for c in new_password):
            print("Password must contain at least one digit.")
            return 'False'
            
        confirm_password = input("Confirm new password: ")
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            return 'False'
                    
        data['users'][username]["password"] = new_password
        save_data(data)
        return 'True'
    else:
        print("Incorrect current password.")
        return 'False'
        







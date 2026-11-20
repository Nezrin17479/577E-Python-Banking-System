import hashlib
import time
from datetime import datetime, timedelta
from storage import save_data


def blocked_user(seconds=60):
    print("Too many failed login attempts.")
    for remaining_time in range(seconds, -1, -1):
        
        print(f"\rPlease wait: 00:{remaining_time:02d} ", end="")
        time.sleep(1)
    print("\nYou may try again.\n")
    return 1

def check_login(now,data, username, password):
    if username in data["users"]:
        if now < data["users"][username]["lockout_until"]:
            left_second=int((data["users"][username]["lockout_until"]-now).total_seconds())
            k=blocked_user(left_second)
            data["users"][username]["lockout_until"]='None'
            save_data(data)
        else:
            data["users"][username]["lockout_until"]='None'
            k=1
            save_data(data)

        if k==1:
            if data["users"][username]["card_status"]=='active':
                main_password=data["users"][username]["password"]
                hash_object_user=hashlib.sha256(main_password.encode('utf-8'))
                hashed_result_user=hash_object_user.hexdigest()

                accessed_password=hashlib.sha256(password.encode('utf-8'))
                accessed_password_result=accessed_password.hexdigest()
                if hashed_result_user==accessed_password_result:
                    data["users"][username]["failed_attempts"]=0
                    data['users'][username]['last_login'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    save_data(data) 
            
                    return True
                else:

                    data["users"][username]["failed_attempts"]+=1
                    save_data(data) 

                    return False
            else:
                return failed_attempts()
    else:
        return '2'

def failed_attempts(now,data,username):
    if data["users"][username]["failed_attempts"]==3 or data["users"][username]["failed_attempts"]==6:
        if data["users"][username]["failed_attempts"]==3:
            blocked_user(seconds=60)==1
            data["users"][username]["lockout_until"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            return True
        else:
            data["users"][username]["card_status"]='blocked'
            save_data(data) 
            return False
    
        







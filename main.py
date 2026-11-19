from storage import load_data

def main():
    data = load_data()
    print("Sistem işə düşdü, istifadəçi sayı:", len(data["users"]))

if __name__ == "__main__":
    main()
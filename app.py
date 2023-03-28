import os
import json
import datetime
import api.openapi as openapi

with open('data.json', 'r') as f:
    data = json.load(f)
    data = json.dumps(data)

today = datetime.datetime.now().strftime("%A, %B %d, %Y")

def cls():
    os.system('cls')

while True:
    cls()
    print("Today: " + today)
    print("")
    print("[1] Get Day-Plan")
    print("[2] View & Edit Profile")
    print("[3] Exit")
    print("")
    choice = input("Enter your choice: ")
    if choice == "1":
        cls()
        print("Sending Request...")
        res = openapi.get_dayplan(data, today)
        print("\n\n\n" + res)
        input("Press Enter to continue...")
    elif choice == "2":
        cls()
        print("Sending Request...")
        res = openapi.get_dayplan(data, today)
        print("\n\n\n" + res)
        input("Press Enter to continue...")
    elif choice == "3":
        exit()
    else:
        cls()
        print("Invalid Choice!")
        input("Press Enter to continue...")
import json

def collect_user_data():
    name = input("What's your name? ")
    age = input("How old are you? ")

    user_data = {
        "name": name,
        "age": age
    }

    with open('user_data.json', 'w') as file:
        json.dump(user_data, file, indent=4)

    print("Data has been saved to user_data.json.")

collect_user_data()
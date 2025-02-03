import json

def read_user_data():
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)

        print("User Data:")
        print(f"Name: {user_data['name']}")
        print(f"Age: {user_data['age']}")

    except FileNotFoundError:
        print("The file user_data.json does not exist.")

    read_user_data()
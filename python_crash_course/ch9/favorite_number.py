import json

def favorite_number_data():
    username = input("What's your favorite number? ")

    with open("python_crash_course\\ch9\\favorite_number.json", "w") as f:
        json.dump(username, f)

favorite_number_data()
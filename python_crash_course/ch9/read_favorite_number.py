import json 

def favorite_number_data():
    username = input("What's your favorite number? ")

    with open("python_crash_course\\ch9\\favorite_number.json", "w") as f:
        json.dump(username, f)

favorite_number_data()

def read_the_favorite_number():
    filename = "python_crash_course\\ch9\\favorite_number.json"
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
            print("The number is already stored")
    except FileNotFoundError:
        None
    else:
        return username
    
favorite_number = read_the_favorite_number()
print(favorite_number)
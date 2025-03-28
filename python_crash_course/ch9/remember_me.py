import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'python_crash_course\\ch9\\username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'python_crash_course\\ch9\\username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

def verify_user():
    user_input = input("what's the name of the user?")
    if user_input == get_stored_username():
        greet_user()
    else:
        get_new_username()
verify_user()
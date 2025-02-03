def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num 
    return total

result = sum_all(1, 2, 3, 4, 5) # numbers = (1, 2, 3, 4, 5)
print(result) #output: 15

def greet(**info):
    name = info.get("name", "Friend") # Handle potential missing key
    age = info.get("age")
    message = f"Hello, {name}!"
    if age:
        message += f" You are {age} years old."
    print(message)

greet(name="Bob", age=30) # info = {"name", "Bob", "age": 30}

def create_user(name, *permissions, age=None, city=None):
    """
    Creates a user profile with a name , optional permission, age, and city.
    
    Args:
        name: The user's name (required).
        *permissions: A variable number of permissions (optional).
        age: The user's age (optional).
        city: The user's city (optional).
        
    Returns:
        A diciotionary containing the user profile information
    """
    user_profile = {
        "name": name,
        "permissions": list(permissions), # Convert args to a list
    }

    # Add optional arguments (age and city) if provided using kwargs
    if age:
        user_profile["age"] = age
    if city:
        user_profile["city"] = city
    
    return user_profile

# Example usage with different combinations of arguments
user1 = create_user("Alice", "read", "write")
user2 = create_user("Bob", age=30, city="New York")
user3 = create_user("Charlie", "admin", "delete", age=25)

print(user1)
print(user2)
print(user3)
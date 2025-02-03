class User:
    def __init__(self, first_name, last_name, address, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.address}")
        print(f"{self.age}")
        print(f"{self.country}")

class Admin(User):
    def __init__(self, first_name, last_name, address, age, country):
        super().__init__(first_name, last_name, address, age, country)
        self.privileges = ["can add post", "can delete post", "can ban user"]


class Privileges(Admin):
    def __init__(self, first_name, last_name, address, age, country):
        super().__init__(first_name, last_name, address, age, country)
        
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

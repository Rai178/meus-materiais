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
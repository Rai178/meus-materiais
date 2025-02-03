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

user = User("Raí", "Sousa", "Itanhangá", "24", "Brazil")
user1 = User("Eduardo", "Bichona", "Itanhangá", "30", "Brazil")
user2 = User("Valtecir", "Eskenazi", "Itanhangá", "60", "Brazil" )

user.describe_user()
user1.describe_user()
user2.describe_user()
        
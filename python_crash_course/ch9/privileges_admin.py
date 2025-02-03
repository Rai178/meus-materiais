import user_class

class Admin(user_class.User):
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
class User:

    def __init__(self, name, last_name, password, location, field):
      self.name = name 
      self.last_name = last_name
      self.password = password
      self.location = location
      self.field = field
      self.login_attempts = 0

    def increment_login_attempts(self):
       self.login_attempts += 1

    def reset_login_attempts(self):
       self.login_attempts = 0

user1 = User('rai', 'santos', '178178', 'rio de janeiro', 'software' )
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"{user1.login_attempts}")
       
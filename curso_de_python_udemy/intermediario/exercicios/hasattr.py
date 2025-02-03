class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("alice", 30)

print(hasattr(person, 'name'))
print(hasattr(person, 'address'))
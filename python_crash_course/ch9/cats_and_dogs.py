file_cat = "python_crash_course/ch9/cats.txt"
file_dog = "python_crash_course\ch9\dog.txt"
try:
    with open(file_cat, 'r') as cat:
        print(cat.read())

    with open(file_dog, 'r') as dog:
        print(dog.read())
except FileNotFoundError:
    pass
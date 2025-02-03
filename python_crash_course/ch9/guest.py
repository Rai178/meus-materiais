file = "python_crash_course\ch9\guest.txt"
name = input("what's your name?")

with open(file, 'w') as guest:
    guest.write(name)
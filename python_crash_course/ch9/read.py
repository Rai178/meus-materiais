file = "python_crash_course/ch9/learning_python.txt"

with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


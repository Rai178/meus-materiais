filename = "python_crash_course/ch9/learning_python.txt"

with open(filename, "r", encoding="utf-8") as file:
    str = file.read()

new_str = str.replace('python', 'C')

with open(filename, "w", encoding='utf-8') as file:
    file.write(new_str)

print(str)

    


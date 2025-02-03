files = "python_crash_course/ch9/names.txt"

with open(files, 'a') as response:
    while True:
        responses = input("Why do you like programming?")
        response.write(f'{responses}\n')

        if responses == "exit":
            break
        
while True:
    name = input("What's your name?")
    
    if name == 'exit':
        break
    else:
        print(f"nice to meet your {name}")
        file = "python_crash_course\ch9\guest_book.txt"
        
        try:
            with open(file, 'a') as recording:
                recording.write(f"The user {name} has entered their name.\n")
            print(f"Name {name} written to file.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
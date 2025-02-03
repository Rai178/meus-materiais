while True:
    try:
        number1 = int(input("Give me a number: "))
        number2 = int(input("Give me another number: "))
        print(number1 + number2)
    except ValueError:
        print("You need to prompt a number to me.")
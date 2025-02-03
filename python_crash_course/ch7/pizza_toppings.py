#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
#pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.
dictionary = {}

while not dictionary: 
    pizza = input("what flavor of pizza do you want? ")
    if pizza == 'quit':
        break
    topping = input("What coverage do you want? ")
    dictionary[pizza] = topping

print (dictionary)

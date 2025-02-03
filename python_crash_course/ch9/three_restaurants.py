class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open")

restaurant = Restaurant('Le monde', 'Bigger')
print(f'{restaurant.restaurant_name}, {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('Fronteira', 'Bigger')
restaurant2 = Restaurant('Parme', 'Small')
restaurant3 = Restaurant('Cuchara', 'Bigger')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
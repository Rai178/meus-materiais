class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        return number_served
    
    def increment_number_served(self, increment):
        self.number_served += increment
        

restaurant = Restaurant('Le monde', 'Bigger', 10)
print(f'{restaurant.restaurant_name}, {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()
number_served = restaurant.set_number_served(60)
print(f"Number served: {number_served}")
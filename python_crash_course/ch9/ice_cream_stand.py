class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open")

class IceCreamStand(Restaurant):
    """Represent the ice cream flavors"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.ice_cream_flavors = ['chocolate', 'baunilha', 'banana']

    def flavors(self):
        return self.ice_cream_flavors

flavor = IceCreamStand('turino', 'large')
print(flavor.flavors())

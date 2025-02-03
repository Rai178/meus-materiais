from random import randint
class Die:
    
    def __init__(self, value=6):
        self.value = value
    
    def roll_die(self):
        print(randint(1, self.value))
        return 

dice = Die(20).roll_die()
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))

die6 = Die()
die6.roll_die()

die10 = Die(10)
die10.roll_die()

die20 = Die(20)
die20.roll_die()
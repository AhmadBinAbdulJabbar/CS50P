import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in ", random.choice(cls.houses))

# hat = Hat()
# # hat1 = Hat()
# hat.sort("Harry")

Hat.sort("Harry")

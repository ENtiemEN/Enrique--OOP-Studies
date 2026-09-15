import random

class Hat:
    # def __init__(self):
    #     self.houses: list = ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    houses: list = ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # <-- Class variable

    @classmethod
    def sort(cls, name: str) -> None:
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")

Hat().sort("Enrique")

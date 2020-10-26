# Class Definition
class Fruit:
    # Constructor
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I'm {self.name}"


# Object instantiation/creation
apple = Fruit("Apple")
print(apple)

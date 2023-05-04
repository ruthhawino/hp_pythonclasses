class Fruit:
    is_edible = True

    def __init__(self, name, color, is_sweet):
        self.name = name
        self.color = color
        self.is_sweet = is_sweet

    def wash(self):
        print("The fruit is being washed.")

    def peel(self):
        print("The fruit is being peeled.")

    def eat(self):
        print("The fruit is being eaten.")

fruit1 = Fruit("Apple", "Red", True)
fruit1.wash()

fruit2 = Fruit("Banana", "Yellow", True)

fruit2.eat()
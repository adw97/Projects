class Bot:
    def __init__(self, name, weight, color):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print(f"My name is {self.name}")

b1 = Bot("Tom", "red", 30)
b2 = Bot("Jerry", "blue", 40)

b1.introduceSelf()
b2.introduceSelf()



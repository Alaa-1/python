from pet import Pet


class Dog(Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)

    def noise(self):
        print("whof whof")
        return self

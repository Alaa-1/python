class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 25
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("sqlmkdjfnazefjqsfijaze")
        return self


dog = Pet("Spike", "Dog", "fetch", 100, 65)
ninjach = Ninja("jona", "sedwik", "bubbly", "cookie", dog)

ninjach.feed().walk().bathe()

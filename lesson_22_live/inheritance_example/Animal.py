class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.species} {self.name} is eating")

    def sleep(self):
        print(f"{self.species} {self.name} is sleeping")

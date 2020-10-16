class Animal():
    def __init__(self, age, name, species_name, number_of_limbs):
        self.age = age
        self.name = name
        self.species_name = species_name
        self.number_of_limbs = number_of_limbs

    def talk(self):
        print("Привіт")

    def eat(self):
        print("Їсть")
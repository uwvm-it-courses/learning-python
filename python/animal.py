class Animal:
    def __init__(self,  name, species_name="Animal", age=1, number_of_limbs=4):
        self.age = age
        self.name = name
        self.species_name = species_name
        self.number_of_limbs = number_of_limbs

    def talk(self):
        print("Привіт")

    def eat(self):
        print("Їсть")


class Dog(Animal):
    def __init__(self, name, breed, spacies_name='Dog', age=1, number_of_limbs=4):
        super().__init__(name, spacies_name, age, number_of_limbs)
        self.breed=breed

    def talk(self):
        print(f'{self.species_name} {self.breed} {self.name} каже гав-гав')

dog1 = Dog('Bob', 'мопс')

dog1.talk()
dog1.eat()


class Dog:
    species = "Canis Familiaris"   # Class Variable

    def __init__(self, breed, age):
        self.breed = breed         # Instance Variable 1
        self.age = age             # Instance Variable 2

    def display(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age)
        print()


# Objects of two different breeds
dog1 = Dog("Labrador", 3)
dog2 = Dog("German Shepherd", 5)

dog1.display()
dog2.display()
class Dog:
    animal = "dog"  # Nahian sir is bad mao
    def __init__(self, name, breed, size, temperament, food):
        self.name = name
        self.breed = breed
        self.size = size
        self.temperament = temperament
        self.food = food

# Farhan is good mao
dog1 = Dog("Papu", "German Shepherd", "Large", "Loyal", "Dry Kibble")
dog2 = Dog("Doge", "Labrador Retriever", "Large", "Friendly", "Wet Food")
dog3 = Dog("Woo", "Chihuahua", "Small", "Alert", "Soft Food")

# Aditya is Suiiii
for dog in (dog1, dog2, dog3):
    print(f"animal: {dog.animal}")
    print(f"name: {dog.name}")
    print(f"breed: {dog.breed}")
    print(f"size: {dog.size}")
    print(f"temperament: {dog.temperament}")
    print(f"food: {dog.food}\n")
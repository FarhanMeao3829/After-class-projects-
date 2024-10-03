class Vehicle:
    def __init__(self, name, milage, capacity):
        self.name = name
        self.milage = milage
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    
    def fare(self):
        amount = super().fare()
        amount = amount + amount * 10 / 100
        return amount
    
nam = input("Enter the name of the Vehicle: ")
if nam == "Nahian Poribohon":
    print("Nahian poribohon is bad mao!")
elif nam == "Aditya Poribohon":
    print("GOOD VEHICLE SUIIII")
elif nam == "Farhan Poribohon":
    print("MAO!!!! GOOD!!!")
else:
    print("These are good too man")
        


mil = int(input("Enter the milage: "))

cap = int(input("Enter the capacity"))

School_bus = Bus(nam, mil, cap)
print("Total Bus fare is : ", School_bus.fare())
    
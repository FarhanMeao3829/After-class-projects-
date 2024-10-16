class Lamborghini:
    def drive(self):
        print("Lamborghini is a fast and cool car ")
        
    def mileage(self):
        print("Lamborghini mileage is approximately 10-15 km/l")
        
    def max_speed(self):
        print("Lamborghini max speed is over 300 km/h and faster than Tata nano")

class TataNano:
    def drive(self):
        print("Tata nano is a small cute car")
        
    def mileage(self):
        print("Tata Nano mileage is approximately 20-25 km/l")
        
    def max_speed(self):
        print("Tata Nano max speed is about 65-70 km/h and it's slow")

objLambo = Lamborghini()
objNano = TataNano()

for car in (objLambo, objNano):
    car.drive()
    car.mileage()
    car.max_speed()
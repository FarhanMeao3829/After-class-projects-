class Circle:
    
    def __init__(self, r):
        self.r = r
        
    def area(self):
            return 3.1416* (self.r**2)
        
    def circuu(self):
            return 2*3.1416*self.r
    
    
radius = float(input("Enter the radius plz : "))
circ1 = Circle(radius)
               
               
print(f"Radius: {radius}")
print(f"Area: {circ1.area()}")
print(f"Circumference: {circ1.circuu()}")
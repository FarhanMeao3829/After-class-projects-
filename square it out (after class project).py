ran = int(input("Enter the range: "))

squa = []

for i in range(0, ran+1):
    y = i**2
    squa.append(y)
    
print(squa)

for i in squa:
    if i % 2 == 0:
        print(f"{i} is EVEN")
        
    else:
        print(f"{i} is ODD")
        
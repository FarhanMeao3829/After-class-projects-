num = int(input("Enter a number mao: "))

li = []

for i in range(0, num+1):
    li.append(i)
    

odd = [x for x in li if x%2 != 0]

print(odd)

#=============================================================================

fruits = ["apple", "banana", "orange"]

newFruits = []

newFruits.append(fruits[0].capitalize())
newFruits.append(fruits[1].capitalize())
newFruits.append(fruits[2].capitalize())

print(newFruits)
        


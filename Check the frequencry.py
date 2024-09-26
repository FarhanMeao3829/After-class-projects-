test_dict = {
    'Codingal' : 2,
    'Is' : 2,
    'Best' : 2,
    'For' : 1,
    'Coding' : 1
}

print("The original dictionary : " + str(test_dict))

k = 2

res = 0 

for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
        
print("Frequency of K is : " + str(res))
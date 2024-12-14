import random

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

length = 12

password = ''

for _ in range(length):
    char_type = random.choice([lowercase, uppercase, digits])
    password += random.choice(char_type)

print(f"Your random password is: {password}")
import random

lowercase_alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]
uppercase_alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]
digits = [str(i) for i in range(0, 10)]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'
]

password = ""
user_lower = int(input("How many lower character alphabets would you like in your password : "))
user_upper = int(input("How many upper character alphabets would you like in your password : "))
user_digits = int(input("How many digits would you like in your password : "))
user_symbols = int(input("How many symbols would you like in your password : "))

for i in range(user_lower):
    password = password + random.choice(lowercase_alphabets)

for i in range(user_upper):
    password = password + random.choice(uppercase_alphabets)

for i in range(user_digits):
    password = password + random.choice(digits)

for i in range(user_symbols):
    password = password + random.choice(symbols)

l = list(password)
random.shuffle(l)
result = ''.join(l)

print(result)





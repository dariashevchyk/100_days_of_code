import random
alphabet_lower = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
digits_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'
]

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password? "))
symbols_1 = int(input("How many symbols would you like? "))
numbers_1 = int(input("How many numbers would you like? "))
password = []
for char in range(0, letters):
    password.append(random.choice(alphabet_lower))
for char in range(0, symbols_1):
    password.append(random.choice(symbols))
for char in range(0, numbers_1):
    password.append(random.choice(digits_str))

print(password)
random.shuffle(password)
print(password)

password_str = ""
for char in password:
    password_str += char
print(f"Your password is: {password_str}")
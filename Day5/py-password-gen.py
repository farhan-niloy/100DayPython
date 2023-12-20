import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

ltr = []
emoji = []
num = []

for l in range(0, nr_letters):
    rand_letters = random.randint(0, len(letters) -1)
    ltr.append(letters[rand_letters])
    l += 1
print(ltr)

for s in range(0, nr_symbols):
    rand_symbols = random.randint(0, len(symbols)-1)
    emoji.append(symbols[rand_symbols])
    s += 1
print(emoji)

for n in range(0, nr_numbers):
    rand_numbers = random.randint(0, len(numbers)-1)
    num.append(numbers[rand_numbers])
    n += 1
print(num)

join = ltr + emoji + num
print(join)

#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:

#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
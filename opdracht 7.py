import random
x = random.randrange(10)
print(x)

while True:
    y = input("Gok het juiste getal: ")
    if int(y) == x:
        print("Gelukt!")
        break
    else:
        print("Helaas!")

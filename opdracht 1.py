x = input("Hoe groot?")
y = int(x)

for i in range(0, y):
    for j in range(0, i + 1):
        print("*", end="")
    print("\r")

for i in range(y, 0, -1):
    for j in range(0, i - 1):
        print("*", end="")
    print("\r")

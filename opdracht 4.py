#VERSIE 1
def palindroom(x):
    y = ''.join(reversed(x))
    print(y)
    if x == y:
        print(x, "is WEL een Palindroom!")
    else:
        print(x, "is GEEN Palindroom.")

palindroom(x = "racecar")

#VERSIE 2
def palindroom(x):
    reversedString = []
    index = len(x)
    while index > 0:
        reversedString += x[index - 1]
        index = index - 1
    for i in reversedString:
        print(i, end="")


palindroom(x="abcdegf")
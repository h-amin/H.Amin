getallen = [0, 2, 3, 3, 5, 6, 10, 13, 11, 5, 5, 0, 1, 2, 3, 4, 2]
occurences = []
binarylst= [0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0 ,0 ,0 ,1]
difference = []

# opdracht 3a)
def count(x):
    for n in getallen:
        if n == x:
            occurences.append((n))
    print("Het getal", x, "komt", len(occurences),"maal in het getallen lijst voor")


count(x=7)

# opdracht 3b)
def getallenDiff():
    for i in range(0, len(getallen) - 1):
        x = abs(getallen[i] - getallen[i+1])
        difference.append(x)
    biggest_diff = max(difference)
    return biggest_diff


getallenDiff()

# opdracht 3c) Ik heb uiteindelijk een nieuw functie gemaakt omdat ik niet weet hoe ik het probleem moet oplossen
# Probleem: Als ik tweemaal de count functie will gebruiken dan telt de tweede count functie het lijstje tweemaal.
def binaryfunct():
    if binarylst.count(1) > binarylst.count(0):
        print("Succes!")
    elif binarylst.count(0) > 12:
        print("Er mogen niet meer dan 12 nullen zijn.")
    else:
        print("Error.")


binaryfunct()
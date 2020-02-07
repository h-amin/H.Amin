file = open("random.txt", "r")
f = file.readlines()
file = open("zonderspatiestxt", "w")

lst = []

for i in f:
    line = i.strip()
    lst.append(line)
    if line == "":
        lst.remove(line)
print(lst)

for i in lst:
    file.write(i)
    file.write("\n")
file.close()


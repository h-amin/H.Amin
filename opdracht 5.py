lst = [0, 2, 3, 6, 7, 5, 10 ,22, 11, 12, 44, 56, 3, 4, 66, 45, 6]

def sorteerGetallen(x):
    for index in range(1, len(x)):
        value = x[index]
        i = index - 1
        while i >= 0:
            if value < x[i]:
                x[i+1] = x[i]
                x[i] = value
                i = i - 1
            else:
                break
    print(x)


sorteerGetallen(x=lst)
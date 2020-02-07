import random
random_lst = list(range(10))
i = 0

random.shuffle(random_lst)
print(random_lst)


# (1)


def avg_lst(x):
    n = sum(x)
    y = n / len(x)
    print(y)

avg_lst(x=random_lst)


# (2)
lst_b = [[1, 3, 2, 5, 6], [2, 4, 0, 6, 7], [6, 6, 4, 6, 5], [1, 5, 2, 9, 9]]
lst_c = []


def avg_multiple_lst(z):
    for i in range(len(z)):
        n = sum(z[i])
        m = n / len(z[i])
        lst_c.append(m)
        q = sum(lst_c)
        p = q / (len(lst_c))
    print(p)


avg_multiple_lst(z=lst_b)

lst = [0,1,2,20,8,60,10]
lengte_lst = len(lst)


max_verschil = 0
for i in range(0, lengte_lst-1):
    verschil = abs(lst[i] - lst[i+1])
    if verschil > max_verschil:
        max_verschil = verschil
        print(max_verschil)
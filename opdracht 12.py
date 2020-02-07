def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == False and i % 5 == False:
            print('fizzbuzz')
            continue
        if i % 3 == False:
            print("fizz")
        elif i % 5 == False:
            print("buzz")
        else:
            print(i)


fizzbuzz()

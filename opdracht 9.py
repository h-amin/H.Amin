def cyclisch_verschuiven(ch, n):
    x = list(ch)
    for i in range(0, len(x)):
        x[i] = int(x[i])

    if n > 0:
        print(x[n:] + x[:n])
    elif n < 0:
        print(x[n:] + x[:n])


cyclisch_verschuiven(ch="1011000", n=3) #VB 1
cyclisch_verschuiven(ch="1011100", n=-4) #VB 2

def sequence(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, 20):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    print(fibonacci_numbers[n])
sequence(10)
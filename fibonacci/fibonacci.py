def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 1:
        return fibonacci(n - 1) + fibonacci(n - 2)


for x in range(9):
    print(fibonacci(x))
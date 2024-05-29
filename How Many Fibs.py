def count_fibonacci(a, b):
    fib_numbers = [1, 2]
    while fib_numbers[-1] <= b:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return sum(1 for num in fib_numbers if a <= num <= b)

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(count_fibonacci(a, b))

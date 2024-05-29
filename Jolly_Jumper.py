def is_jolly(a):
    diff = set(abs(a[i] - a[i+1]) for i in range(len(a)-1))
    return len(diff) == len(a) - 1 and min(diff) > 0

n = int(input())
sequence = list(map(int, input().strip().split()))

if is_jolly(sequence):
    print("Jolly")
else:
    print("Not jolly")

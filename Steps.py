def min_steps(x, y):
    diff = y - x 
    if diff % 2 == 0:
        return diff // 2 + 1
    else:
        return diff // 2 + 2

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print(min_steps(x, y))

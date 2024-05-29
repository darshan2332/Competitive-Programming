import sys

ans = [0] * 10001
exp = 1

ans[0] = 0
count = 1
i = 1

while i <= 10000:
    j = count
    while i <= 10000 and j > 0:
        ans[i] = ans[i - 1] + exp
        i += 1
        j -= 1
    count += 1
    exp <<= 1

for line in sys.stdin:
    n = int(line.strip())
    print(ans[n])

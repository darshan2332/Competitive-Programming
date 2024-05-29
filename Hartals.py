def hartals(n, p, hartal_para):
    lost_days = 0
    for day in range(1, n + 1):
        if day % 7 == 6 or day % 7 == 0:  
            continue
        for party in hartal_para:
            if day % party == 0:
                lost_days += 1
                break
    return lost_days

t = int(input())
for _ in range(t):
    n = int(input())
    p = int(input())
    hartal_para = []
    for _ in range(p):
        parameter = int(input())
        hartal_para.append(parameter)
    print(hartals(n, p, hartal_para))

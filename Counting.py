from sys import stdin

def generate_table(num):
    t = [0,2,5,13]
    for n in range(4,num+1):
        t.append(2*t[n-1]+t[n-2]+t[n-3])
    return t

Table = generate_table(1000)

while True:
    line = stdin.readline()
    if not line:
        break
    print(Table[int(line)])

import sys
a = int(input())
b = []
for _ in range(a):
    c = list(map(int,input().split(' ')))
    b.append(c)

bs = []
for z in range(4):
    for i in range(a):
        bs = sorted(b, key=lambda x: x[i])
        if b == bs:
            for j in range(a):
                bs[j] = sorted(b[j])
            if b == bs:
                for x in range(a):
                    print(*b[x])
                sys.exit()
    b = [[b[j][a-1-i] for j in range(a)] for i in range(a)]


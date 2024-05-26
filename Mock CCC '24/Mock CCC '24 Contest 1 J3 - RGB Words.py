n = int(input())
a = input()
ans = 0
b = []

for i in range(n):
    if a[i] == 'R':
        b.append('R')
    elif a[i] == 'G':
        for j in b:
            if j[0] == 'R' and 'G' not in j:
                j += 'G'
    else:
        for j in b:
            if 'R' in b and 'G' in b:
                j += 'B'
print(b.count('RGB'))
    
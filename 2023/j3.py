n = int(input())
a = [input() for _ in range(n)]
c = []
for i in range(5):
    count = 0
    for j in range(n):
        if a[j][i] == 'Y':
            count += 1
    c.append(count)
m = max(c)
ans = ''
for i in range(5):
    if c[i] == m:
        ans += str(i+1)
print(','.join(ans))
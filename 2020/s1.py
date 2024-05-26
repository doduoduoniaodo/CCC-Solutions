n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split(' '))))

a.sort()

ans = 0

for i in range(n-1):
    speed = abs((a[i+1][1]-a[i][1]) / (a[i+1][0]-a[i][0]))
    ans = max(ans, speed)

print(ans)
# Solution 1:
import sys

n = int(input())
weathers = [input() for _ in range(n)]

if 'P' not in weathers:
    print(n-1)
    sys.exit()

left = 0
rain = 0
ans = 0

for right in range(n):
    if weathers[right] == 'P':
        rain += 1
    
    while rain > 1:
        if weathers[left] == 'P':
            rain -= 1
        left += 1
    
    ans = max(ans, right - left + 1)

print(ans)


# Solution 2: 
n = int(input())
a = []
start = -1
mx = 0
for i in range(n):
    c = input()
    if c == 'P':
        if start != -1:
            a.append((start, i-1))
            mx = max(mx, i-start)
            start = -1
    else:
        if start == -1:
            start = i
if start != -1:
    a.append((start, n-1))
    mx = max(mx, n-start)
if mx == n:
    print(n-1)
else:
    ans = mx+1
    for i in range(1, len(a)):
        if a[i-1][1] + 2 == a[i][0]:
            ans = max(ans, a[i][1] - a[i-1][0] + 1)
    print(ans)


n = int(input())
ans = 0
for _ in range(n):
    p = int(input())
    f = int(input())
    s = p * 5 - f * 3
    if s > 40:
        ans += 1
if ans == n:
    print(str(ans) + '+')
else:
    print(ans)
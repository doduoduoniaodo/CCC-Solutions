t = int(input())
c = int(input())
a = [int(input()) for _ in range(c)]
a.sort()
time = 0
ans = 0
while time <= t:
    if a[ans] + time <= t:
        time += a[ans]
        ans += 1
    else:
        break
print(ans)
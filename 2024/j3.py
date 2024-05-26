n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
m = 0
cnt = 0
ans = 0
ans1 = ''
y = False
for i in range(n):
    if m != a[i]:
        m = a[i]
        cnt += 1
    if cnt == 3:
        ans1 = a[i]
        ans += 1
        y = True
    if cnt != 3 and y:
        break
print(ans1, ans) 
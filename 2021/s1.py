a = int(input())
b = input().split(' ')
c = input().split(' ')
ans = 0
for i in range(a):
    if i < a:
        ans += (int(b[i])+int(b[i+1])) * int(c[i]) / 2

print(ans)
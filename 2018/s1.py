a = []
for _ in range(int(input())):
    a.append(int(input()))
a.sort()
ans = float('inf')
for i in range(1, len(a)-1):
    b = round((a[i]-a[i-1])/2, 1) + round((a[i+1]-a[i])/2, 1)
    if b < ans:
        ans = b
print(ans)
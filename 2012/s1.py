j = int(input())
ans = 0
for a in range(1, j-2):
    for b in range(a+1, j-1):
        for c in range(b+1, j):
            ans += 1
print(ans)
j = int(input())
a = int(input())
jerseys = [input() for _ in range(j)]
ans = 0
for _ in range(a):
    size, n = input().split()
    n = int(n) - 1
    if jerseys[n] <= size:
        ans += 1
        jerseys[n] = 'a'
print(ans)
n = int(input())
a = [0] + [int(input()) for i in range(n-1)]
ways = [1]*(n+1)
for i in range(1, n):
    ways[i] += 1
    ways[a[i]] *= ways[i]
print(ways[n])
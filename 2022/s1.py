import sys
input = sys.stdin.readline

n = int(input())

# n = 4a + 5b

ans = 0

for i in range(n//4+1):
    if (n - 4*i) % 5 == 0:
        ans += 1

print(ans)
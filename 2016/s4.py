import sys
input = sys.stdin.readline

n = int(input())
riceballs = list(map(int, input().split()))

psa = [0]*(n+1)
ans = 0
dp = [[False]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    psa[i] = riceballs[i-1]
    ans = max(ans, psa[i])
    dp[i][i] = True
    psa[i] += psa[i-1]

for len in range(2, n+1):
    l = 1
    r = l+len-1
    while r <= n:
        p = l
        q = r
        while p < q:
            if (dp[l][p] and dp[q][r] and (p+1==q or dp[p+1][q-1]) and (psa[p]-psa[l-1]) == (psa[r]-psa[q-1])):
                dp[l][r] = True
                break
            if (psa[p]-psa[l-1]) < (psa[r]-psa[q-1]):
                p += 1
            else:
                q -= 1
        if dp[l][r]:
            ans = max(ans, psa[r]-psa[l-1])
        l += 1
        r += 1

print(ans)

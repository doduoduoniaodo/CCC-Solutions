# difference array + prefix sum array

import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
q = int(input())

diff = [0] * (n+2)
for _ in range(l):
    p, s = map(int, input().split())
    l = max(1, p-s)
    r = min(n, p+s)
    diff[l] += 1
    diff[r+1] -= 1

psa = [0] * (n+2)
psa[0] = diff[0]
for i in range(1, n+2):
    psa[i] = psa[i-1] + diff[i]

for _ in range(q):
    if psa[int(input())] > 0:
        print('Y')
    else:
        print('N')

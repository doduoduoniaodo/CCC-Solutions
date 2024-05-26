import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
s = sorted(set(arr))
c = Counter(arr)
print(s[-3],c[s[-3]])
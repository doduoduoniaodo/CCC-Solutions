import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
mid_index = math.ceil(n/2)
low = sorted(a[:mid_index], reverse=True)
high = a[mid_index:]
for i in range(n//2):
    print(low[i], high[i], end=' ')
if n % 2 == 1:
    print(low[-1])
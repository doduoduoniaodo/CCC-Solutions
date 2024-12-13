from bisect import bisect_right
import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
must_dock = [int(input()) for _ in range(p)]
gates = [i for i in range(1, g+1)]

ans = 0
for i in must_dock:
    last = bisect_right(gates, i)-1     #find the index of last element <= i
    if last < 0:
        break
    else:
        ans += 1
        gates.pop(last)

print(ans)
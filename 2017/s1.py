import sys
input = sys.stdin.readline

n = int(input())
swifts = list(map(int, input().split()))
semaphores = list(map(int, input().split()))

ans = 0
total_swifts = 0
total_semaphores = 0
for i in range(n):
    total_swifts += swifts[i]
    total_semaphores += semaphores[i]
    if total_swifts == total_semaphores:
        ans = i+1
print(ans)
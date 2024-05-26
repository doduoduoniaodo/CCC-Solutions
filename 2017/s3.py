import sys
input = sys.stdin.readline

f = [0] * 2001
n = int(input())
for i in list(map(int, input().split())):
    f[i] += 1
cnt = [0] * 4002
for i in range(1, len(f)):
    for j in range(i, len(f)):
        if i == j:
            cnt[i+j] += f[i]//2
        else:
            cnt[i+j] += min(f[i], f[j])
mx = max(cnt)
print(mx, cnt.count(mx))


'''
n = int(input())
l = list(map(int, input().split()))
arr = [0] * 2001
sums = [0] * 4002
length = 1
heights = 0

for i in range(n):
    arr[l[i]] += 1

for i in range(2001):
    if arr[i] > 0:
        for j in range(i, 2001):
            if i == j:
                sums[i + j] += arr[j] // 2
            else:
                sums[i + j] += min(arr[i], arr[j])

for s in sums:
    if s > length:
        length = s
        heights = 1
    elif s == length:
        heights += 1

print(length, heights)
'''
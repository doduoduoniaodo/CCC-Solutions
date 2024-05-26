import sys
input = sys.stdin.readline
n = int(input())
freq = [0] * 1001
for i in range(n):
    freq[int(input())] += 1
mx, a = max(freq), []
for i in range(len(freq)):
    if freq[i] == mx:
        a.append(i)
if len(a) > 1:  # multiple highest frequency
    print(a[-1] - a[0])
else:
    mx2, b = sorted(freq.copy())[-2], [] # 2nd highest frequency
    for i in range(len(freq)):
        if freq[i] == mx2:
            b.append(i)
    print(max(abs(b[0] - a[0]), abs(b[-1] - a[0])))
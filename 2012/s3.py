import sys
input = sys.stdin.readline

n = int(input())
freq = [0] * 1001
for _ in range(n):
    freq[int(input())] += 1

# 1st highest frequency
max_f = max(freq)
a = []
for i in range(len(freq)):
    if freq[i] == max_f:
        a.append(i)

if len(a) > 1:  # multiple 1st highest frequency
    print(a[-1] - a[0])
else:
    # 2nd highest frequency
    second_max_f = sorted(freq.copy(), reverse=True)[1]
    b = []
    for i in range(len(freq)):
        if freq[i] == second_max_f:
            b.append(i)
    
    print(max(abs(max(a) - min(b)), abs(min(a) - max(b))))

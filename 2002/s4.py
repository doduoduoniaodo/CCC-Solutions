m = int(input())
q = int(input())
names = []
times = []
for _ in range(q):
    names.append(input())
    times.append(int(input()))

dp = [float('inf')]*(q+1)
dp[0] = 0
group_size = [0]*(q+1)

for i in range(1, q+1):
    cur_max = 0
    for j in range(1, min(m, i)+1):
        cur_max = max(cur_max, times[i-j])
        if dp[i-j] + cur_max < dp[i]:
            dp[i] = dp[i-j] + cur_max
            group_size[i] = j

groups = []
i = q
while i > 0:
    k = group_size[i]
    groups.append(names[i-k: i])
    i -= k

print("Total Time:", dp[-1])
for i in reversed(groups):
    print(' '.join(i))


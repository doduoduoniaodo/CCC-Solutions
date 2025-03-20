import sys
input = sys.stdin.readline

r, c, m = int(input()), int(input()), int(input())

def get_cell(i, j):
    return (i*c + j) % m + 1

dp_prev = [float('inf')] *c
dp_curr = [float('inf')] *c
for i in range(c):
    dp_prev[i] = get_cell(0, i)

for i in range(1, r):
    # first column
    dp_curr[0] = min(dp_prev[0], dp_prev[1]) + get_cell(i, 0)
    # last column
    dp_curr[c-1] = min(dp_prev[c-2], dp_prev[c-1]) + get_cell(i, c-1)
    # middle columns
    for j in range(1, c-1):
        dp_curr[j] = min(dp_prev[j-1], dp_prev[j], dp_prev[j+1]) + get_cell(i, j)

    dp_prev, dp_curr = dp_curr, dp_prev

print(min(dp_prev))

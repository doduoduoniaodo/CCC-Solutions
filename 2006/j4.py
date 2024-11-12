import sys
input = sys.stdin.readline

adj_after = {1:[2], 2:[], 3:[], 4:[1, 3], 5:[3], 6:[], 7:[1]}

while True:
    x, y = int(input()), int(input())
    if (x, y) == (0, 0):
        break
    adj_after[y].append(x)

for i in range(1, 8):
    adj_after[i].sort()

ans = []
for _ in range(7):
    for i in range(1, 8):
        if i not in ans and len(adj_after[i]) == 0:
            ans.append(i)
            for j in range(1, 8):
                if i in adj_after[j]:
                    adj_after[j].remove(i)
            break

if len(ans) == 7:
    print(*ans)
else:
    print('Cannot complete these tasks. Going to bed.')
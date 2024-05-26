n, t = int(input()), int(input())
tree = []
for i in range(t):
    tree.append(list(map(int, input().split())))
tree.append([0, 0])
tree.append([n+1, n+1])
ans = 0
for i in range(len(tree)):
    for j in range(i+1, len(tree)):
        left = min(tree[i][1], tree[j][1])
        right = max(tree[i][1], tree[j][1])
        middle = []
        for k in range(t):
            if left < tree[k][1] < right:
                middle.append(tree[k][0])
        middle.append(0)
        middle.append(n+1)
        middle.sort()
        for k in range(1, len(middle)):
            ans = max(ans, min(middle[k] - middle[k-1] - 1, right - left - 1))
print(ans)
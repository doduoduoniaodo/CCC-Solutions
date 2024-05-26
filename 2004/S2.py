from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
a = [[0, i, 0] for i in range(n)]  #yodeller i [total score, index, worst ranking]
for _ in range(k):
    p = list(map(int, input().split()))
    for i in range(n):
        a[i][0] += p[a[i][1]]
    a.sort(reverse=True)
    rank = 0
    for i in range(n):
        if i == 0 or a[i][0] != a[i-1][0]:
            rank = i + 1
        a[i][2] = max(a[i][2], rank)
a.sort(key=lambda x: (-x[0], x[1]))
top = a[0][0]
for score, idx, worst in a:
    if score == top:
        print(f"Yodeller {str(idx+1)} is the TopYodeller: score {str(score)}, worst rank {str(worst)}")
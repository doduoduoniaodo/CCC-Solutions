n = int(input())
a = [list(map(int, input().split(' '))) for _ in range(n)]
ans_a, ans_d = 100, 100
for i in range(n):
    if a[i][0] > a[i][1]:
        ans_d -= a[i][0]
    elif a[i][0] < a[i][1]:
        ans_a -= a[i][1]
print(ans_a)
print(ans_d)
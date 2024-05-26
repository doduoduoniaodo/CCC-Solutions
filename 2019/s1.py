a = input()
ans = [1, 2, 3, 4]
for i in range(len(a)):
    if a[i] == 'H':
        ans[0], ans[2] = ans[2], ans[0]
        ans[1], ans[3] = ans[3], ans[1]
    else:
        ans[0], ans[1] = ans[1], ans[0]
        ans[2], ans[3] = ans[3], ans[2]

print(ans[0], ans[1])
print(ans[2], ans[3])
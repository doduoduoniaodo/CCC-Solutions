ans = ['A', 'B', 'C', 'D', 'E']
y = True

while y:
    a = int(input())
    b = int(input())
    for i in range(b):
        if a == 1:
            ans.append(ans[0])
            ans.pop(0)
        elif a == 2:
            ans.insert(0, ans[4])
            ans.pop()
        elif a == 3:
            ans[0], ans[1] = ans[1], ans[0]
        elif a == 4:
            for x in ans:
                    print(x, end=' ')
            y = False
            break
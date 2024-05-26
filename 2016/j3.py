a = input()
ans = []
b = 0
for i in range(len(a)):
    for j in range(0, len(a)-b):
        c = a[j:j+b+1]
        if c == c[::-1]:
            ans.append(len(c))
    b += 1
if len(ans) != 0:
    print(max(ans))
else:
    print(1)
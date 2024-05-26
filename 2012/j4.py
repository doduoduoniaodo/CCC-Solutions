k = int(input())
a = input()
ans = ''
for i in range(len(a)):
    s = ord(a[i]) - k - 3*(i+1)
    if s < 65:
        ans += chr(90-(65-s-1))
    else:
        ans += chr(s)
print(ans)
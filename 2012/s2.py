a = input()
s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ans = 0
for i in range(0, len(a), 2):
    if i <= len(a)-3:
        if s[a[i+1]] < s[a[i+3]]:
            ans -= int(a[i]) * s[a[i+1]]
        else:
            ans += int(a[i]) * s[a[i+1]]
    else:
        ans += int(a[i]) * s[a[i+1]]
print(ans)
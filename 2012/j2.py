a, b, c, d = [int(input()) for _ in range(4)]
if a == b == c == d:
    print('Fish At Constant Depth')
elif a < b < c < d:
    print('Fish Rising')
elif a > b > c > d:
    print('Fish Diving')
else:
    print('No Fish')
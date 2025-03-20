n = int(input())
weathers = [input() for _ in range(n)]

left = 0
rain = 0
ans = 0

for right in range(n):
    if weathers[right] == 'P':
        rain += 1
    
    while rain > 1:
        if weathers[left] == 'P':
            rain -= 1
        left += 1
    
    ans = max(ans, right - left + 1)

if 'P' not in weathers:
    ans -= 1

print(ans)
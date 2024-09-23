import sys
input = sys.stdin.readline

'''
idea: 
    put consecutive same number in B into segments 
    use 2 pointers to find a[i] which corresponds to a segment 
    if L < i , swipe left  [L, i]
    if R > i, swipe right [i , R]
'''

# step 1: read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print('YES\n0')
    sys.exit()

# step 2: get segments for array B
segments = []
r = 0
t = b[0]
for i in range(n):
    if b[i] != t:
        segments.append((r, i-1))
        r = i
        t = b[i]
segments.append((r, n-1))

# step 3: find which a[i] for segments[j] using 2 pointers
i = 0
left = []
right = []
for l, r in segments:
    while i < n and a[i] != b[l]:
        i += 1
    
    if i == n:
        print('NO')
        sys.exit()
    else:
        if l < i:
            left.append((l, i))
        if r > i:
            right.append((i, r))


print('YES')
print(len(left) + len(right))
for i in left:
    print('L', i[0], i[1])
for i in range(len(right)-1, -1, -1):
    print('R', right[i][0], right[i][1])


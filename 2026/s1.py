import sys
input = sys.stdin.readline

a, b, k, t = int(input()), int(input()), int(input()),int(input())

distance = abs(b - a)

n = distance // k
r = distance % k

options = [n + r,           # 1. n giant hops + r baby hops
           n + r + 2,       # 2. after at the destination by method 1., 1 baby hop forwards + 1 backwards
           n+1 + k-r,       # 3. n+1 giant hops + return back      
           n+1 + k-r + 2,   # 4. after at the destination by method 3., 1 baby hop forwards + 1 backwards
           distance,        # 5. all small jumps
           distance + 2     # 6. after at the destination by method 5., 1 baby hop forwards + 1 backwards
           ]

if n > 0:
    options.append(n-1 + (distance - k*(n-1)))  # 7. taking one fewer giant hop and making up the remaining distance with baby hops

# remove duplicates and sort
options = sorted(set(options))
if t == 1:
    print(options[0])
else:
    print(options[1])

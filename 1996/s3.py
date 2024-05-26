import sys
input = sys.stdin.readline

def f(s, ones, zeroes):
    if ones == 0 and zeroes == 0:
        print(s)
        return
    
    if ones > 0:
        f(s+'1', ones-1, zeroes)
    if zeroes > 0:
        f(s+'0', ones, zeroes-1)

a = int(input())

for i in range(a):
    n, k = map(int, input().split())
    print('The bit patterns are')
    f('', k, n-k)
    if i == a-1:
        continue
    print()
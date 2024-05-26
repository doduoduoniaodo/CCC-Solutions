import sys
input = sys.stdin.readline

crystal_blk = [(1, 0), (2, 0), (3, 0), (2, 1)]
partial_blk = [(1, 1), (2, 2), (3, 1)]

def isCrystal(m, x, y):
    blk = 5**(m-1)
    bx, by = x//blk, y//blk
    if (bx, by) in crystal_blk:
        return True
    elif (bx, by) in partial_blk:
        if m == 1: return False
        return isCrystal(m-1, x % blk, y % blk)
    else:
        return False

for _ in range(int(input())):
    m, x, y = map(int, input().split())
    print('crystal' if isCrystal(m, x, y) else 'empty')
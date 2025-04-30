import sys
input = sys.stdin.readline
from functools import lru_cache

reactions = [
        (2, 1, 0, 2),  # AABDD
        (1, 1, 1, 1),  # ABCD
        (0, 0, 2, 1),  # CCD
        (0, 3, 0, 0),  # BBB
        (1, 0, 0, 1)   # AD
    ]

@lru_cache(None)
def f(a, b, c, d):
    for ra, rb, rc, rd in reactions:
        na, nb, nc, nd = a-ra, b-rb, c-rc, d-rd
        if na >= 0 and nb >= 0 and nc >= 0 and nd >= 0:
            if not f(na, nb, nc, nd):
                return True
    return False

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print("Patrick" if f(a, b, c, d) else "Roland")


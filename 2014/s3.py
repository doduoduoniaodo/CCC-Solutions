import sys
input = sys.stdin.readline

for _ in range(int(input())):
    car = [int(input()) for i in range(int(input()))]
    branch, expect = [], 1
    for x in reversed(car):
        branch.append(x)
        while branch and branch[-1] == expect:
            branch.pop()
            expect += 1
    print('Y' if len(branch) == 0 else 'N')
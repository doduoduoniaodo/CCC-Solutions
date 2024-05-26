import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    t = int(input())
    Round = 0
    undefeated = t
    oneloss = 0
    eliminated = 0
    while True:
        print(f'Round {Round}: {undefeated} undefeated, {oneloss} one-loss, {eliminated} eliminated')
        if undefeated == 0 and oneloss == 1:
            break
        if undefeated == 1 and oneloss == 1:
            oneloss = 2
            undefeated = 0
        else:
            eliminated = eliminated + oneloss // 2
            oneloss = oneloss - (oneloss // 2) + (undefeated // 2)
            undefeated = undefeated - undefeated // 2
        Round += 1
    if i != n-1:
        print(f'There are {Round} rounds.\n')
    else:
        print(f'There are {Round} rounds.')
    
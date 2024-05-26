str1 = input()
R = int(input())
C = int(input())
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1) ,(0, -1), (-1, -1)]
grid = [input().split() for _ in range(R)]
ans = 0
def func1(r, c, direction, currentidx, turn_yet):
    global ans
    # BASE CASE
    if currentidx == len(str1):
        ans += 1
    else:
        newr, newc = r + dir[direction][0], c + dir[direction][1]
        if 0 <= newr < R and 0<= newc < C and grid[newr][newc] == str1[currentidx]:
            func1(newr, newc, direction, currentidx + 1, turn_yet)
        if not turn_yet:
            newr, newc = r + dir[(direction + 2)%8][0], c + dir[(direction + 2) % 8][1]
            if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == str1[currentidx]:
                func1(newr, newc, (direction + 2) % 8, currentidx + 1, True)
            newr, newc = r + dir[(direction + 6) % 8][0], c + dir[(direction + 6) % 8][1]
            if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == str1[currentidx]:
                func1(newr, newc, (direction + 6) % 8, currentidx + 1, True)




for r in range(R):
    for c in range(C):
        # if there is a letter identical to the first letter of the word
        if grid[r][c] == str1[0]:
            # check every 8 directions that the next letter could be on
            for d in range(8):
                # move to the next letter depending on the current direction
                newr, newc = r + dir[d][0], c + dir[d][1]
                # check if the new letter is the second letter of the word AND that it is IN BOUND
                if 0 <= newr < R and 0 <= newc < C and grid[newr][newc] == str1[1]:
                    # call the function and continue searching
                    func1(newr,newc,d,2,False)
                    # func1(current row, current column, current direction, second letter of the word, didn't turn yet)

print(ans)


'''
import sys
input = sys.stdin.readline

word = input().strip()
R, C = int(input()), int(input())
g = [input().strip().split() for i in range(R)]
ways = 0
dir = [(-1, 0), (-1, 1),  (0, 1), (1, 1) , (1, 0) , (1, -1) , (0, -1), (-1, -1)]

def fun(r, c, k, idx, turn):
    global ways
    if idx == len(word):
        ways += 1
        return
    for i in range(k-2, k+3, 2):
        nk = (i + 8) % 8
        nr, nc = r + dir[nk][0], c + dir[nk][1]
        if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == word[idx] and (nk == k or not turn):
            fun(nr, nc, nk, idx+1, turn or nk != k)

for i in range(R):
    for j in range(C):
        if g[i][j] == word[0]:
            for k in range(8):
                ni, nj = i + dir[k][0], j + dir[k][1]
                if 0 <= ni < R and 0 <= nj < C and g[ni][nj] == word[1]:
                    fun(ni, nj, k, 2, False)
print(ways)
'''
import sys
input = sys.stdin.readline

# Monkey word:    A-word   or   A-word + N + Monkey word
# A-word :     A   or   B + monkey word + S

def isMonkeyWord(word):
    if len(word) == 0: return False
    if isAWord(word): return True
    for i in range(len(word)):
        if word[i] == 'N' and isAWord(word[:i]) and isMonkeyWord(word[i+1:]):
            return True
    return False

def isAWord(word):
    if len(word) == 0: return False
    if word == 'A': return True
    if len(word) >= 3 and word[0] == 'B' and word[-1] == 'S' and isMonkeyWord(word[1:-1]):
        return True
    return False

while True:
    word = input().strip()
    if word == 'X':
        break
    print('YES') if isMonkeyWord(word) else print('NO')
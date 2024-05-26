a = []
b = input()
num_L = 0
num_M = 0
num_S = 0
ans = 0

for i in range(len(b)):
    a.append(b[i])
    if b[i] == 'L':
        num_L += 1
    elif b[i] == 'M':
        num_M += 1
    else:
        num_S += 1

section_L = [0] * 3
section_M = [0] * 3
section_S = [0] * 3
for s1 in range(0, num_L):
    if a[s1] == 'L':
        section_L[0] += 1
    elif a[s1] == 'M':
        section_L[1] += 1
    else:
        section_L[2] += 1
for s2 in range(num_L, (num_M+num_L)):
    if a[s2] == 'L':
        section_M[0] += 1
    elif a[s2] == 'M':
        section_M[1] += 1
    else:
        section_M[2] += 1
for s3 in range(num_M+num_L, (num_M+num_S+num_L)):
    if a[s3] == 'L':
        section_S[0] += 1
    elif a[s3] == 'M':
        section_S[1] += 1
    else:
        section_S[2] += 1

if section_S[0] != 0:
    ans += section_S[0]
    section_L[0] += section_S[0]
    if section_L[2] < section_S[0]:
        section_S[2] += section_L[2]
        section_S[1] += (section_S[0]-section_L[2])
        section_L[1] -= (section_S[0]-section_L[2])
        section_L[2] = 0
    else:
        section_S[2] += section_S[0]
        section_L[2] -= section_S[0]
    section_S[0] = 0

if section_M[0] != 0:
    ans += section_M[0]
    section_L[0] += section_M[0]
    if section_L[1] < section_M[0]:
        section_M[1] += section_L[1]
        section_M[2] += (section_M[0]-section_L[1])
        section_L[2] -= (section_M[0]-section_L[1])
        section_L[1] = 0
    else:
        section_M[1] += section_M[0]
        section_L[1] -= section_M[0]
    section_M[0] = 0

if section_S[2] != num_S:
    ans += section_M[2]


print(ans)
t = [int(input()), int(input())]
i = 2
while True:
    t.append(t[i-2] - t[i-1])
    if t[i] > t[i-1]:
        print(len(t))
        break
    i += 1
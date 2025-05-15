from collections import deque
adjacent_list = {i: set() for i in range(0, 51)}
adjacent_list[1].add(6);adjacent_list[2].add(6);adjacent_list[3].update(set([4, 5, 6, 15]));adjacent_list[4].update(set([3, 5, 6]));adjacent_list[5].update(set([3, 4, 6]));adjacent_list[6].update(set([1, 2, 3, 4, 5, 7]));adjacent_list[7].update(set([6, 8]));adjacent_list[8].update(set([7, 9]));adjacent_list[9].update(set([8, 10, 12]));adjacent_list[10].update(set([9, 11]));adjacent_list[11].update(set([10, 12]));adjacent_list[12].update(set([9, 11, 13]));adjacent_list[13].update(set([12, 14, 15]));adjacent_list[14].add(13);adjacent_list[15].update(set([3, 13]));adjacent_list[16].update(set([17, 18]));adjacent_list[17].update(set([16, 18]));adjacent_list[18].update(set([16, 17]))
while True:
    command = input()
    if command == 'q':
        break
    elif command == 'i':
        x, y = int(input()), int(input())
        adjacent_list[x].add(y)
        adjacent_list[y].add(x)
    elif command == 'd':
        x, y = int(input()), int(input())
        adjacent_list[x].remove(y)
        adjacent_list[y].remove(x)
    elif command == 'n':
        print(len(adjacent_list[int(input())]))
    elif command == 'f':
        x = int(input())
        ans = set()
        for i in adjacent_list[x]:
            ans.update(adjacent_list[i])
        ans -= adjacent_list[x]
        if x in ans:
            ans.remove(x)
        print(len(ans))
    elif command == 's':
        x, y = int(input()), int(input())
        queue = deque([(x, 0)])
        visited = [False] * 51
        visited[x] = True
        while queue:
            current, distance = queue.popleft()
            if current == y:
                print(distance)
                break
            for i in adjacent_list[current]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, distance+1))
        else:
            print('Not connected')
    
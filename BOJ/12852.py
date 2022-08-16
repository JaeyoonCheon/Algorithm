"""
12852번 1로 만들기 2
"""

import collections

X = int(input())

pos = [[] for _ in range(X + 1)]

q = collections.deque()

q.append((X, X, 0))

while q:
    curr = q.popleft()

    if curr[0] == 1:
        break

    if curr[0] % 3 == 0:
        q.append((curr[0] // 3, curr[0], curr[2] + 1))
        if pos[curr[0] // 3]:
            if curr not in pos[curr[0] // 3] and pos[curr[0] // 3][0][2] >= curr[2]:
                pos[curr[0] // 3].append(curr)
        else:
            pos[curr[0] // 3].append(curr)

    if curr[0] % 2 == 0:
        q.append((curr[0] // 3, curr[0], curr[2] + 1))
        if pos[curr[0] // 2]:
            if curr not in pos[curr[0] // 2] and pos[curr[0] // 2][0][2] >= curr[2]:
                pos[curr[0] // 2].append(curr)
        else:
            pos[curr[0] // 2].append(curr)

    if curr[0] - 1 > 0:
        q.append((curr[0] - 1, curr[0], curr[2] + 1))
        if pos[curr[0] - 1]:
            if curr not in pos[curr[0] - 1] and pos[curr[0] - 1][0][2] >= curr[2]:
                pos[curr[0] - 1].append(curr)
        else:
            pos[curr[0] - 1].append(curr)

result = []

while True:
    result.append(curr[0])
    if curr[0] == curr[1]:
        break

    for i in pos[curr[1]]:
        if i[0] == curr[1] and i[2] == curr[2] - 1:
            curr = i
            break

result.reverse()

print(len(result) - 1)
for i in result:
    print(i, end=" ")

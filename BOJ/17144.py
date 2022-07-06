"""
17144번 미세먼지 안녕!

1.  전형적인 구현문제로, 단계별로 문제의 조건을 잘 살펴보고!!
    부분적으로 함수를 만들어가면서 해결하면 어렵지 않게 풀이할 수 있다.
"""

import copy

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

circulator = []

for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            circulator.append((i, j))
            circulator.append((i + 1, j))


def checkBorder(x, y):
    if x < 0 or x >= R or y < 0 or y >= C:
        return False
    return True


def checkCirculator(x, y):
    if room[x][y] == -1:
        return False
    return True


def expansion(x, y, newRoom):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    isExpanse = [False] * 4
    currentAmount = room[x][y]

    for i in range(4):
        if checkBorder(x + dx[i], y + dy[i]) and checkCirculator(x + dx[i], y + dy[i]):
            isExpanse[i] = True

    canExpanse = isExpanse.count(True)

    for i in range(4):
        if isExpanse[i]:
            newRoom[x + dx[i]][y + dy[i]] += currentAmount // 5

    newRoom[x][y] += room[x][y] - currentAmount // 5 * canExpanse


def diffusion():
    newRoom = [[0] * C for _ in range(R)]

    current = [
        list(map(lambda x: False if x <= 0 else True, room[i])) for i in range(R)
    ]

    for i in range(R):
        for j in range(C):
            if current[i][j]:
                expansion(i, j, newRoom)

    for i in circulator:
        newRoom[i[0]][i[1]] = -1

    return newRoom


def circulation():
    upper, lower = circulator[0], circulator[1]

    for i in range(upper[0], 0, -1):
        room[i][0] = room[i - 1][0]
    for i in range(C - 1):
        room[0][i] = room[0][i + 1]
    for i in range(upper[0]):
        room[i][C - 1] = room[i + 1][C - 1]
    for i in range(C - 1, 0, -1):
        room[upper[0]][i] = room[upper[0]][i - 1]
    room[upper[0]][upper[1] + 1] = 0
    room[upper[0]][upper[1]] = -1

    for i in range(lower[0], R - 1):
        room[i][0] = room[i + 1][0]
    for i in range(C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    for i in range(R - 1, lower[0], -1):
        room[i][C - 1] = room[i - 1][C - 1]
    for i in range(C - 1, 0, -1):
        room[lower[0]][i] = room[lower[0]][i - 1]
    room[lower[0]][lower[1] + 1] = 0
    room[lower[0]][lower[1]] = -1


for i in range(T):
    room = copy.deepcopy(diffusion())
    circulation()

total = 0
for i in room:
    total += sum(i)

total += 2

print(total)

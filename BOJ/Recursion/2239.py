"""
2239번 스도쿠

1.  초기 시도:
    어떤 빈 칸에 대해 가로/세로/3x3구역에 대해 1~9 중 하나만 들어갈 수 있을 경우
    그 칸을 바꾸는 방식으로 로직을 구성
    ->  hiddlen single을 고려하지 않았고 여러가지 위 논리로만 구할 수 없는 해답이 있어
    결과가 나오지 않음

2.  백트래킹
    위의 기본 조건들을 가지고 빈 칸의 왼쪽 위부터 차례대로 하나 씩 가능한 수를 놓아보는
    백트래킹을 접목했고 가능한 수를 작은 수부터 놓기 때문에 가장 먼저 찾게되는 가능한 정답이
    모든 가능한 경우 중 가장 작은 수의 경우이다.
"""

import sys, copy

puzzle = [list(map(int, list(input()))) for _ in range(9)]

caches = [[[True] * 10 for _ in range(9)] for _ in range(9)]

case = []

next = 0


def checkHorizon(cache, pos):
    for i in range(9):
        if i == pos[1]:
            continue
        if cache[puzzle[pos[0]][i]]:
            cache[puzzle[pos[0]][i]] = False


def checkVertical(cache, pos):
    for i in range(9):
        if i == pos[0]:
            continue
        if cache[puzzle[i][pos[1]]]:
            cache[puzzle[i][pos[1]]] = False


def checkArea(cache, pos):
    areaH, areaV = pos[0] // 3, pos[1] // 3

    for i in range(areaH * 3, (areaH + 1) * 3):
        for j in range(areaV * 3, (areaV + 1) * 3):
            if i == pos[0] and j == pos[1]:
                continue
            if cache[puzzle[i][j]]:
                cache[puzzle[i][j]] = False


def dfs(pos):
    isBlank = False
    for i in range(pos[0], 9):
        if i == pos[0]:
            for j in range(pos[1], 9):
                if puzzle[i][j] == 0:
                    isBlank = True
                    break
        else:
            for j in range(9):
                if puzzle[i][j] == 0:
                    isBlank = True
                    break
        if isBlank:
            break

    if not isBlank:
        for i in range(9):
            print("".join(str(c) for c in puzzle[i]))
        sys.exit(0)

    nextPos = (i, j)

    prevCache = copy.deepcopy(caches[i][j])

    checkHorizon(caches[i][j], nextPos)
    checkVertical(caches[i][j], nextPos)
    checkArea(caches[i][j], nextPos)

    for idx, v in enumerate(caches[i][j][1:]):
        if v:
            puzzle[i][j] = idx + 1
            dfs(nextPos)
            puzzle[i][j] = 0

    caches[i][j] = prevCache


dfs((0, 0))

minValue = float("inf")
minIdx = -1

""" for idx, v in enumerate(case):
    num = ""
    for j in range(9):
        s = "".join(str(c) for c in v[j])
        num = num + s
    num = int(num)

    if num < minValue:
        minValue = num
        minIdx = idx """

""" latestPuzzle = case[0]

for i in range(9):
    print("".join(str(c) for c in latestPuzzle[i])) """

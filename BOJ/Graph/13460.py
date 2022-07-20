"""
13460번 구슬 탈출 2

1.  미로를 탈출하는 최단경로를 찾는 문제의 변형이라고 생각되는 문제.

2.  보드에서 출구 "O"를 찾아 빨간 공을 내보내야 하는데, 보드에는 빨간 공과 파란 공이 있으며
    보드판을 기울여 두 공을 움직인 후, 빨간 공만(!) 탈출시켜야 한다.

3.  BFS로 큐에 넣으면 탈출하는 경우를 찾는 즉시 종료하므로 최단 움직임을 찾을 수 있는데,
    공이 2개이므로 공의 좌표를 두 공 모두 저장하여 사용해야만 한다.
    또한 메모이제이션을 한 공의 좌표에 대한 다른 공의 좌표이므로 4차원을 사용하는 것이 편리할 것이다.

4.  문제에서 제시하는 기울임이란 상/하/좌/우로 움직이는데, 기울여서 두 공 모두 움직이지 않을때
    한 기울임이 종료되는것으로 보고 두 공은 서로 겹쳐지지 않는다.

5.  BFS 미로찾기 문제에서 추가해 두 공의 위치를 비교해
    1)  두 공이 더 이상 벽에 막혀 움직이지 않을 떄 큐에 저장
    2)  두 공 모두 탈출했을 경우 큐에 저장 x
    3)  빨간 공만 탈출했을 경우 종료하고 움직인 횟수를 반환
    4)  파란 공만 탈출했을 경우 큐에 저장 x

6.  이 문제에서 유의할 점은 기울이는 방향에 따라 먼저 움직여야 하는 공이 정해지는 것이다.
    따라서, 기울이는 순서에 따라 공의 색깔을 기록해놓아야 한다.    
"""

import collections, copy

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS():
    q = collections.deque()
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    initRed, initBlue = 0, 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                initRed = (i, j)
            elif board[i][j] == "B":
                initBlue = (i, j)
            else:
                continue

    q.append((initRed[0], initRed[1], initBlue[0], initBlue[1], 0))
    visited[initRed[0]][initRed[1]][initBlue[0]][initBlue[1]] = True

    while q:
        curr = q.popleft()
        red = [curr[0], curr[1]]
        blue = [curr[2], curr[3]]
        moved = curr[4]

        for i in range(4):
            step = 1
            isFirstGoal, isSecondGoal = False, False

            currRed, currBlue = copy.deepcopy(red), copy.deepcopy(blue)
            order = [currRed, currBlue]

            first, second = "Red", "Blue"

            # 우(실 좌표)
            if i == 0:
                if currRed[0] == currBlue[0]:
                    if currRed[1] < currBlue[1]:
                        order[0], order[1] = order[1], order[0]
                        first, second = second, first
            # 하(실 좌표)
            elif i == 1:
                if currRed[1] == currBlue[1]:
                    if currRed[0] < currBlue[0]:
                        order[0], order[1] = order[1], order[0]
                        first, second = second, first
            # 좌(실 좌표)
            elif i == 2:
                if currRed[0] == currBlue[0]:
                    if currRed[1] > currBlue[1]:
                        order[0], order[1] = order[1], order[0]
                        first, second = second, first
            # 상(실 좌표)
            elif i == 3:
                if currRed[1] == currBlue[1]:
                    if currRed[0] > currBlue[0]:
                        order[0], order[1] = order[1], order[0]
                        first, second = second, first

            while True:
                nextX = order[0][0] + dx[i]
                nextY = order[0][1] + dy[i]

                if board[nextX][nextY] == "O":
                    order[0] = [nextX, nextY]
                    isFirstGoal = True
                    break
                elif board[nextX][nextY] == "#":
                    break
                else:
                    order[0] = [nextX, nextY]

            while True:
                nextX = order[1][0] + dx[i]
                nextY = order[1][1] + dy[i]

                if board[nextX][nextY] == "O":
                    order[1] = [nextX, nextY]
                    isSecondGoal = True
                    break
                elif [nextX, nextY] == order[0]:
                    break
                elif board[nextX][nextY] == "#":
                    break
                else:
                    order[1] = [nextX, nextY]

            if isFirstGoal and isSecondGoal:
                continue
            elif isFirstGoal and first == "Red":
                return moved + 1
            elif isFirstGoal and first != "Red":
                continue
            elif isSecondGoal and second == "Red":
                return moved + 1
            elif isSecondGoal and second != "Red":
                continue
            else:
                if first != "Red":
                    order[0], order[1] = order[1], order[0]
                if not visited[order[0][0]][order[0][1]][order[1][0]][order[1][1]]:
                    visited[order[0][0]][order[0][1]][order[1][0]][order[1][1]] = True
                    q.append((order[0][0], order[0][1], order[1][0], order[1][1], moved + 1))
                else:
                    continue

    return -1


result = BFS()

if result != -1:
    if result <= 10:
        print(result)
    else:
        print(-1)
else:
    print(-1)

"""
12100번 2048 (Easy)

1.  유명한 게임인 2048을 최대 20*20크기의 보드판에서 구현하여 5번 움직였을 때
    만들어지는 최대의 수를 구하는 문제.

2.  익히 아는것 처럼 한 쪽 방향으로 모든 블럭들이 움직이면서 같은 수인 블럭이
    만난다면 움직이는 방향쪽에 있는 블럭으로 두 블럭이 합쳐진다.
    또한 한 움직임에 합쳐진 블럭은 그 움직임 내에서는 다시 합쳐지는 경우는 없다.

3.  4가지 모듈
    1)  주어진 방향 dir에 따라 모든 블럭들을 이동시키며 같은 수의 블럭이 만날 경우
        합치는 함수.
        상/하/좌/우 4방향에 따라 그 방향의 끝 -1 위치의 블럭부터 주어진 방향으로
        0을 통과하여 같은 수를 만나 합쳐지거나/다른 수를 만나 멈추거나/끝까지 가는 경우를
        조건에 따라 움직이도록 작성
    2)  5번의 상/하/좌/우 움직임을 DFS와 같은 형식으로 재귀호출
    3)  현재 보드판의 최대 수를 찾는 함수
    4)  현재 보드판의 수에 log를 씌워 해당 수의 빈도를 체크하여
        동일한 수가 존재하지 않는다면 탐색을 중단시키는 함수
"""

from math import log
import copy


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

maxNumber = -1
maxPath = ""


def calculation(board, dir):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * N for _ in range(N)]

    if dir == "L":
        for i in range(N):
            for j in range(1, N):
                currIdx = -1

                if board[i][j] == 0:
                    continue
                else:
                    for move in range(1, j + 1):
                        if board[i][j - move] == 0:
                            currIdx = j - move
                            if move == j:
                                board[i][currIdx] = board[i][j]
                                board[i][j] = 0
                                break
                            continue
                        else:
                            if board[i][j - move] == board[i][j]:
                                if not visited[i][j - move]:
                                    visited[i][j - move] = True
                                    board[i][j - move] *= 2
                                    board[i][j] = 0
                                    break
                                else:
                                    if currIdx != -1:
                                        board[i][currIdx] = board[i][j]
                                        board[i][j] = 0
                                        break
                            else:
                                if currIdx == -1:
                                    break
                                board[i][currIdx] = board[i][j]
                                board[i][j] = 0
                            break

    elif dir == "R":
        for i in range(N):
            for j in range(N - 2, -1, -1):
                currIdx = -1
                if board[i][j] == 0:
                    continue
                else:
                    for move in range(1, N - j):
                        if board[i][j + move] == 0:
                            currIdx = j + move
                            if move == N - j - 1:
                                board[i][currIdx] = board[i][j]
                                board[i][j] = 0
                                break
                            continue
                        else:
                            if board[i][j + move] == board[i][j]:
                                if not visited[i][j + move]:
                                    visited[i][j + move] = True
                                    board[i][j + move] *= 2
                                    board[i][j] = 0
                                    break
                                else:
                                    if currIdx != -1:
                                        board[i][currIdx] = board[i][j]
                                        board[i][j] = 0
                                        break
                            else:
                                if currIdx == -1:
                                    break
                                board[i][currIdx] = board[i][j]
                                board[i][j] = 0
                            break
    elif dir == "D":
        for i in range(N):
            for j in range(N - 2, -1, -1):
                currIdx = -1
                if board[j][i] == 0:
                    continue
                else:
                    for move in range(1, N - j):
                        if board[j + move][i] == 0:
                            currIdx = j + move
                            if move == N - j - 1:
                                board[currIdx][i] = board[j][i]
                                board[j][i] = 0
                                break
                            continue
                        else:
                            if board[j + move][i] == board[j][i]:
                                if not visited[j + move][i]:
                                    visited[j + move][i] = True
                                    board[j + move][i] *= 2
                                    board[j][i] = 0
                                    break
                                else:
                                    if currIdx != -1:
                                        board[currIdx][i] = board[j][i]
                                        board[j][i] = 0
                                        break
                            else:
                                if currIdx == -1:
                                    break
                                board[currIdx][i] = board[j][i]
                                board[j][i] = 0
                            break
    elif dir == "U":
        for i in range(N):
            for j in range(1, N):
                currIdx = -1
                if board[j][i] == 0:
                    continue
                else:
                    for move in range(1, j + 1):
                        if board[j - move][i] == 0:
                            currIdx = j - move
                            if move == j:
                                board[currIdx][i] = board[j][i]
                                board[j][i] = 0
                                break
                            continue
                        else:
                            if board[j - move][i] == board[j][i]:
                                if not visited[j - move][i]:
                                    visited[j - move][i] = True
                                    board[j - move][i] *= 2
                                    board[j][i] = 0
                                    break
                                else:
                                    if currIdx != -1:
                                        board[currIdx][i] = board[j][i]
                                        board[j][i] = 0
                                        break
                            else:
                                if currIdx == -1:
                                    break
                                board[currIdx][i] = board[j][i]
                                board[j][i] = 0
                            break

    return board


def findMaxNumber(board):
    maxNum = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] > maxNum:
                maxNum = board[i][j]

    return maxNum


def checkSameNum(board):
    counting = [0] * 21

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                continue
            counting[int(log(board[i][j], 2))] += 1

    for i in range(1, 21):
        if counting[i] > 1:
            return True

    return False


def moving(board, step, path):
    global maxNumber, maxPath
    dir = ["R", "D", "U", "L"]

    currMaxNumber = findMaxNumber(board)
    if currMaxNumber > maxNumber:
        maxNumber = currMaxNumber
        maxPath = path

    if step > 4:
        return

    if checkSameNum(board):
        for i in range(4):
            board_copy = copy.deepcopy(board)
            moving(calculation(board_copy, dir[i]), step + 1, path + dir[i])

    return


moving(board, 0, "")

print(maxNumber)

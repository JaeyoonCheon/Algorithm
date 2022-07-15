"""
9328번 열쇠

1.  문제에서 .은 빈 공간 / *은 벽 / 대문자는 잠긴 문 / 소문자는 열쇠 / $는 문서를 의미한다.
    접근법은 그래프 탐색으로 결정하고 접근해 보았는데,
    문을 열쇠로 열면 새로운 탐색 지점이 생긴다는 점에서 BFS의 Queue가 필요한 문제였다.

2.  우선, 가장자리부터 진입 가능한 지점은 4가지 경우이다.
    1)  빈 공간 .
        =   큐에 추가 + 방문 표시
    2)  열쇠가 놓인 공간 a~z
        =   큐에 추가 + 방문 표시 + 열쇠 꾸러미에 추가 
            + 해당 지점 빈 공간으로 변경
            + 얻은 열쇠로 기록해놨던 잠긴 문 중 열리는 문을 큐에 추가
            + 추가한 문은 방문 표시 및 빈 공간으로 표시
    3)  맞는 열쇠를 가지고 있는 잠긴 문 A~Z
        =   큐에 추가 + 방문 표시
            + 해당 지점 빈 공간으로 변경
    4)  문서가 놓인 공간 $
        =   문서 개수 1 증가 + 큐에 추가 + 방문 표시
            + 해당 지점 빈 공간으로 변경

3.  2에서 추가된 시작 지점들을 가지고 BFS를 실행하면서
    해당 조건에 맞게 상/하/좌/우 4방향을 탐색하며 큐가 빌 때 까지 반복
"""

from calendar import c
import collections

case = []

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def checkBorder(x, y):
    global h, w

    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    else:
        return True


for _ in range(T):
    h, w = map(int, input().split())

    building = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    keys = list(input())
    keepingDoor = []
    count = 0

    q = collections.deque()

    for i in range(h):
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                if building[i][j] == ".":
                    q.append((i, j))
                    visited[i][j] = True
                elif building[i][j].isupper():
                    if building[i][j].lower() in keys:
                        building[i][j] = "."
                        q.append((i, j))
                        visited[i][j] = True
                    else:
                        keepingDoor.append((building[i][j], i, j))
                elif building[i][j].islower():
                    keys.append(building[i][j])
                    building[i][j] = "."
                    q.append((i, j))
                    visited[i][j] = True
                elif building[i][j] == "$":
                    count += 1
                    building[i][j] = "."
                    q.append((i, j))
                    visited[i][j] = True

    while q:
        curr = q.popleft()
        x, y = curr[0], curr[1]

        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]

            if checkBorder(nextX, nextY) and not visited[nextX][nextY]:
                nextPos = building[nextX][nextY]
                if nextPos == ".":
                    q.append((nextX, nextY))
                    visited[nextX][nextY] = True
                elif nextPos.isupper():
                    if nextPos.lower() in keys:
                        q.append((nextX, nextY))
                        visited[nextX][nextY] = True
                        building[nextX][nextY] = "."
                    else:
                        keepingDoor.append((nextPos, nextX, nextY))
                elif nextPos.islower():
                    q.append((nextX, nextY))
                    visited[nextX][nextY] = True

                    if nextPos not in keys:
                        keys.append(nextPos)

                    for door in keepingDoor:
                        if door[0] == nextPos.capitalize():
                            q.append((door[1], door[2]))
                            visited[door[1]][door[2]] = True

                    keepingDoor = [x for x in keepingDoor if x != nextPos]
                    building[nextX][nextY] = "."
                elif nextPos == "$":
                    count += 1
                    q.append((nextX, nextY))
                    visited[nextX][nextY] = True
                    building[nextX][nextY] = "."
                else:
                    continue

    case.append(count)

for i in case:
    print(i)

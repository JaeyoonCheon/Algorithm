"""
16236번 아기 상어

1.  난이도 있는 구현 문제.

2.  문제의 조건을 잘 살펴야 한다.
    1)  초기 아기상어의 크기는 2이다.
    2)  1칸 이동에 걸리는 시간은 1이며 먹는 시간은 없다.
    3)  크기가 같거나 작은 물고기가 있는 칸만 갈 수 있으며, 크가가 같거나 크면 먹지 못한다.
    4)  상하좌우 이동할 수 있으며, 아기상어로부터 거리가 가장 가까운 먹을 수 있는 물고기를 먹으러 간다.
        만약 먹을 수 있는 물고기가 여러 마리 있다면, 위쪽 행 우선 -> 좌측 열 우선으로 향한다.
    5)  먹고 난 후 물고기가 있던 칸은 0이 된다.
    6)  아기상어는 물고기를 자기 크기만큼의 수를 먹으면 크기가 1 성장한다.(2일때 2마리 -> 3)

3.  기본적인 문제 풀이 논리는 현재 위치에서 BFS를 이용한 최단 거리의 먹을 수 있는 물고기 탐색
    -> 이동 후 크기 조정 -> 반복
    
4.  BFS는 다음 순서로 동작한다.
    1)  큐에 저장된 다음 탐색 위치를 꺼낸다.
    2)  해당 위치에서 공간 내에 갈 수 있는 상/하/좌/우 방향을 큐에 넣고,
        아기상어보다 크기가 작은 물고기가 있는 칸을 해당 거리에 물고기가 있는 칸을
        저장하는 canEat 큐에 넣는다.
    3)  canEat큐는 큐에 저장된 바로 다음 칸의 거리가 현재 거리와 다를 때(탐색 거리가 증가할 때)
        canEat큐에 저장된 칸이 있는 지 조사하고 있다면 움직일 물고기가 있는 칸을 찾은 것이다.
    4)  canEat큐에 여러 마리의 물고기가 있다면, 행/열 순서대로 이중 오름차순 정렬을 수행해
        가장 위쪽 / 가장 왼쪽의 물고기를 선택하도록 조정한다.
"""

import collections

N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

currentSize = 2
eatenFish = 0


def checkBorder(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    else:
        False


def findCandidate(x, y):
    visited = [[False] * N for _ in range(N)]
    q = collections.deque()

    q.append((x, y, 0))
    visited[x][y] = True
    space[x][y] = 0

    pick = False
    canEat = []

    while q:
        curr = q.popleft()

        dist = curr[2] + 1

        for dir in range(4):
            if checkBorder(curr[0] + dx[dir], curr[1] + dy[dir]):
                if space[curr[0] + dx[dir]][curr[1] + dy[dir]] > currentSize:
                    continue
                else:
                    if not visited[curr[0] + dx[dir]][curr[1] + dy[dir]]:
                        q.append((curr[0] + dx[dir], curr[1] + dy[dir], dist))
                        visited[curr[0] + dx[dir]][curr[1] + dy[dir]] = True
                        if (
                            space[curr[0] + dx[dir]][curr[1] + dy[dir]]
                            and space[curr[0] + dx[dir]][curr[1] + dy[dir]]
                            != currentSize
                        ):
                            canEat.append((curr[0] + dx[dir], curr[1] + dy[dir], dist))

        if not q or q[0][2] > curr[2]:
            if canEat:
                canEat = sorted(canEat, key=lambda x: (x[0], x[1]))
                pick = canEat[0]
                break

            canEat = []

    if not pick:
        return False
    else:
        space[pick[0]][pick[1]] = 0
        return pick


X, Y = -1, -1
totalTime = 0

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            X, Y = i, j

while True:
    next = findCandidate(X, Y)

    if next:
        elapsedTime = next[2]
        # print(f"{next[0]} {next[1]} ~ {next[2]}")
        totalTime += elapsedTime
        eatenFish += 1
        if eatenFish == currentSize:
            currentSize += 1
            eatenFish = 0
        X, Y = next[0], next[1]
    else:
        break

print(totalTime)

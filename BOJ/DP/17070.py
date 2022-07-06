"""
17070번 파이프 옮기기 1

1.  BFS로 해결하면 편리할 것이라고 생각하여 BFS로 접근하였으나, 각 정점에 여러 번 방문할 수 있고
    이것은 BFS의 방식만을 차용한 완전탐색이 되므로 파이썬으로 시간 초과를 피하기 힘들었다.
    
2.  따라서 DP로 접근해보면 각 칸을 3가지 방향에서 파이프가 전해져 오는 방법의 개수로
    설정하여 시작해보자.
    (0, 1) ~ (0, N-1)까지는 가로 1방법 고정이고
    나머지 칸은 가로 2가지/대각선 3가지/세로 2가지의 케이스를 저장하는 DP배열을 만들어
    N-1/N-1 까지 검사하면 결과값을 구할 수 있다.
    
3.  파이프가 대각선으로 놓일 경우의 벽체 처리를 고려해 주어야 한다!

4.  파이썬은 DFS로 접근하면 DP로 풀이하지 않더라도 완전탐색식으로 가능할 것으로 보인다.
"""

import collections

N = int(input())

home = [list(map(int, input().split())) for _ in range(N)]


def checkBorder(pos):
    x, y = pos[0], pos[1]

    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def checkWall(pos):
    x, y, dir = pos[0], pos[1], pos[2]

    if dir != 1:
        if home[x][y] == 1:
            return False
        return True
    else:
        if home[x - 1][y] == 1 or home[x][y] == 1 or home[x][y - 1] == 1:
            return False
        return True


def checkWallDP(pos, dir):
    x, y = pos[0], pos[1]

    if dir == 0:
        if home[x][y - 1] == 1:
            return False
        return True
    elif dir == 1:
        if home[x - 1][y] == 1 or home[x - 1][y - 1] == 1 or home[x][y - 1] == 1:
            return False
        return True
    else:
        if home[x - 1][y] == 1:
            return False
        return True


def BFS(x, y):
    q = collections.deque()
    case = 0

    if home[N - 1][N - 1] == 1:
        return case

    q.append((x, y, 0))

    while q:
        curr = q.popleft()
        x, y, dir = curr[0], curr[1], curr[2]

        if x == N - 1 and y == N - 1:
            case += 1
            continue

        next = [(x, y + 1, 0), (x + 1, y + 1, 1), (x + 1, y, 2)]

        for i in next:
            if checkBorder(i) and checkWall(i):
                if abs(dir - i[2]) > 1:
                    continue
                q.append(i)

    return case


def DP():
    visited = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    visited[0][1][0] = 1

    if home[N - 1][N - 1] == 1:
        print(0)
        return

    for i in range(0, 1):
        for j in range(2, N):
            if home[i][j] == 0:
                visited[i][j][0] = visited[i][j - 1][0]

    for i in range(1, N):
        for j in range(1, N):
            curr = (i, j)

            if checkWallDP(curr, 0):
                visited[i][j][0] += visited[i][j - 1][0] + visited[i][j - 1][1]
            if checkWallDP(curr, 1):
                visited[i][j][1] += (
                    visited[i - 1][j - 1][0]
                    + visited[i - 1][j - 1][1]
                    + visited[i - 1][j - 1][2]
                )
            if checkWallDP(curr, 2):
                visited[i][j][2] += visited[i - 1][j][1] + visited[i - 1][j][2]

    print(sum(visited[N - 1][N - 1]))


DP()

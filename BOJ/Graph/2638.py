"""
2638번 치즈

1.  치즈가 있고 가장자리는 공기인 판에서 2면 이상 공기와 맞닿은 치즈는 제거하는데 모든 치즈가 녹아 사라지는 시간을
    계산하는 문제로, DFS나 BFS 모두 풀이 가능할 것으로 보인다.
    
2.  가장자리는 항상 공기이므로, 공기끼리 연결된 그래프를 탐색하게 만들고 수행하면서 치즈를 만난다면
    그 만난 횟수를 방문 배열에 저장해놓는다. 이후 탐색이 끝나면 2회 이상 공기와 만난 치즈는 제거하여
    모든 치즈가 제거된 시간을 계산한다.
"""

import sys

sys.setrecursionlimit(100000)

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def checkCheese():
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1:
                return True

    return False


def checkBorder(x, y):
    if x >= N or x < 0 or y >= M or y < 0:
        return False
    return True


def removeCheese(copiedPaper):
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                copiedPaper[i][j] = 0

    return copiedPaper


def DFS(x, y):
    visited[x][y] = True

    for i in range(4):
        nextX, nextY = x + dx[i], y + dy[i]
        if checkBorder(nextX, nextY):
            if paper[nextX][nextY] == 1:
                if visited[nextX][nextY] == False:
                    visited[nextX][nextY] = 1
                else:
                    visited[nextX][nextY] += 1
            else:
                if not visited[nextX][nextY]:
                    visited[nextX][nextY] = True
                    DFS(nextX, nextY)


time = 0

while checkCheese():
    DFS(0, 0)
    paper = removeCheese(paper)
    visited = [[False] * M for _ in range(N)]
    time += 1

print(time)

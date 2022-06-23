"""
2638번 치즈
"""
N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

air = [[False] * M for _ in range(N)]

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
    if x>N and x<0 and y>M and y<0:
        return False
    return True

def DFS(x, y):
    visited[x][y] = True

    for i in range(4):
        nextX,nextY = x+dx[i], y+dy[i]
        if checkBorder(nextX, nextY):
            DFS(nextX, nextY)

while checkCheese():
    
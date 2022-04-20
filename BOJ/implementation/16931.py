"""
16931번 겉넓이 구하기
"""

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

surface = 2 * N * M

for i in range(N):
    # 좌 -> 우
    surface += maps[i][0]
    for j in range(1, M):
        if maps[i][j] > maps[i][j - 1]:
            surface += maps[i][j] - maps[i][j - 1]

for i in range(N):
    # 우 -> 좌
    surface += maps[i][M - 1]
    for j in range(M - 2, -1, -1):
        if maps[i][j] > maps[i][j + 1]:
            surface += maps[i][j] - maps[i][j + 1]

for i in range(M):
    # 상 -> 하
    surface += maps[0][i]
    for j in range(1, N):
        if maps[j][i] > maps[j - 1][i]:
            surface += maps[j][i] - maps[j - 1][i]

for i in range(M):
    # 하 -> 상
    surface += maps[N - 1][i]
    for j in range(N - 2, -1, -1):
        if maps[j][i] > maps[j + 1][i]:
            surface += maps[j][i] - maps[j + 1][i]

print(surface)

"""
16931번 겉넓이 구하기

1.  위+아래 / 오른쪽+왼쪽 / 앞쪽+뒤쪽의 6가지 방향에서 겉넓이가 나타난다.
    위/아래는 무조건 N*M의 넓이로만 나타날 수 있으므로 2*N*M이다.
    
2.  상하좌우의 겉넓이를 구하기 위해, 한 쪽 면에서의 겉넓이를 생각해 보면
    가장 처음 만나는 외곽의 블록의 높이만큼을 처음에 더하고
    이후에 만나는 블록들은 적전의 블록보다 높이가 높을 경우 그 높이의 차만큼이
    겉넓이에 더해진다. 따라서 상하좌우의 겉넓이를 모두 구해 더해주면 결과를 구할 수 있다.
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

"""
15685번 드래곤 커브

1.  '드래곤 커브'란 어떤 점에서 출발하여 어떤 주어진 방향으로 1칸 전진한 직선이 0세대라고 가정하면
    1, 2, 3세대의 드래곤 커브란 그 직전 세대의 드래곤 커브를 시계방향 회전 후 이전 세대의 최종 위치에
    갖다 붙인 커브를 말한다.
    
2.  이것의 규칙성을 찾아보면, n세대는 n-1세대의 행동을 끝 점에서 왼쪽으로 90도 회전 후 그대로 반복한다.
    따라서 진행 거리는 1로 고정되어 있으므로 그 진행 방향만을 고려해 보면
    현 세대의 진행 방향은 이전 세대의 진행 방향을 거꾸로 뒤집은 순서로
    왼쪽 90도 변환 후 동일하게 반복하게 되므로 currDir = (moved[i] + 1) % 4가 적용된다.
    
3.  따라서, 0세대의 두 점을 저장해놓은 후 세대가 진화할 때 마다
    1) 이전세대의 역순 진행 방향 선택 2) 선택한 방향에 90도 변환 3) 변환한 방향으로 전진 후 기록
    4) 변환 완료된 진행 방향을 저장
    순서로 계속해서 진행
"""

N = int(input())

grid = [[False] * 2000 for _ in range(2000)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(N):
    y, x, d, g = map(int, input().split())

    moved = []

    grid[x][y] = True

    currX = x + dx[d]
    currY = y + dy[d]
    grid[currX][currY] = True

    moved.append(d)

    for gen in range(g):
        for i in range(len(moved) - 1, -1, -1):
            currDir = (moved[i] + 1) % 4
            currX = currX + dx[currDir]
            currY = currY + dy[currDir]

            grid[currX][currY] = True

            moved.append(currDir)

count = 0
for i in range(100):
    for j in range(100):
        if (
            grid[i][j] == True
            and grid[i][j + 1] == True
            and grid[i + 1][j] == True
            and grid[i + 1][j + 1] == True
        ):
            count += 1

print(count)

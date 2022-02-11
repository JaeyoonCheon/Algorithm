"""
18290번 NM과 K

1. 2차원 배열로 격자 데이터 입력
2. 백트래킹 방식을 이용하여 visited 리스트에 좌표 튜플을 저장한 뒤 K개를 뽑을 수 있도록
K를 1개 씩 줄여나가면서 재귀 깊이 증가하도록 설계
3. max는 전역변수로 설정, 범위를 고려하여 -20000으로 초기화
4. checkAdj 함수에서 이미 방문한 visited 리스트의 선택된 좌표에 현재 선택한 좌표가 인접하는 지 검사
5. 중요! 백준 시간제한 2초를 지키기 위해 가지치기
selectBlock 함수의 startX 매개변수는 각 재귀 깊이에서 현재 좌표를 선택할 때
가장 최근에 선택된 좌표의 x좌표를 전달하여 그 전의 위치에서 좌표를 선택하지 않도록 가지치기
"""


global max
max = -20000


def checkAdj(x, y, visited):
    for item in visited:
        if item[0] + 1 == x and item[1] == y:
            return False
        if item[0] - 1 == x and item[1] == y:
            return False
        if item[0] == x and item[1] + 1 == y:
            return False
        if item[0] == x and item[1] - 1 == y:
            return False

    return True


def selectBlock(N, M, K, grid, visited, startX, sum):
    global max
    if K == 0:
        if max < sum:
            max = sum
        return
    for x in range(startX, N):
        for y in range(0, M):
            if (x, y) in visited:
                continue
            if checkAdj(x, y, visited) == False:
                continue
            visited.append((x, y))
            selectBlock(N, M, K - 1, grid, visited, x, sum + grid[x][y])
            visited.pop()


N, M, K = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

visited = []

selectBlock(N, M, K, grid, visited, 0, 0)

print(max)

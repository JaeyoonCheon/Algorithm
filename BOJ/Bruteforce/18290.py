"""
18290번 NM과 K
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


def selectBlock(N, M, K, grid, visited, startX, startY, sum):
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
            selectBlock(N, M, K - 1, grid, visited, x, y, sum + grid[x][y])
            visited.pop()


N, M, K = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

visited = []

selectBlock(N, M, K, grid, visited, 0, 0, 0)

print(max)

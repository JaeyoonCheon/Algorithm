"""
2667번 단지 번호 붙이기
"""

N = int(input())

grid = [list(map(int, list(input()))) for _ in range(N)]

visited = [[False] * N for _ in range(N)]


def dfs(x, y, grid, visited):
    global number
    visited[x][y] = True
    number += 1

    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i >= N or x + i < 0:
                continue
            if y + j >= N or y + j < 0:
                continue
            if grid[x + i][y + j] == 0:
                continue
            if visited[x + i][y + j] == True:
                continue
            dfs(x + i, y + j, grid, visited)

    return


number = -1
numbers = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == False and grid[i][j] == 1:
            number += 1
            dfs(i, j, grid, visited)
            numbers.append(number)
            number = 0

numbers.sort()

print(len(numbers))

for i in numbers:
    print(i)

"""
2667번 단지 번호 붙이기

1.  dfs는 일반적으로 동작하는 방식대로 연결된 단지 중 방문하지 않은 집을 방문할 때 마다
    갯수를 증가시켜 따로 저장해놓는다.
    
2.  N*N 격자를 모두 검사하면서 단지에 해당하지만 방문하지 않은 단지를 dfs 실행하여 단지의
    수를 검사한다.
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
            if i == j or i == -1 * j:
                continue
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
            number = -1

numbers.sort()

print(len(numbers))

for i in numbers:
    print(i)

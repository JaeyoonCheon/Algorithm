"""
16724번 피리 부는 사나이

1.  문제 유형을 살펴봤을 때 방향이 정해진 그래프 문제에서 구분된 그래프가 몇 개 인지 구하는 문제로 생각이 되어
    방문체크를 번호로 하는 dfs를 구성하여 풀려고 했었다. 이 방법으로 푸는 중 그래프의 번호를 매기는 데 어려움이 있어 다른 방식을 생각해 보게 되었다.
    
2.  그래프의 구분을 대표적인 알고리즘인 union-find를 응용해 2차원에 매핑시키고 마지막에 다시 root를 갱신시켜준 후 distinct한 값을 count 했다.

3.  다른 사람들의 풀이를 보니 1번에 체크한 방문-번호 방식으로도 count를 셀 수 있었다. 재귀를 하지 않고 화살표를 순회하면서 사이클이 생길 때
    개수를 올려주는 방식으로 하면 시간을 많이 줄일 수 있을 듯 하다.
"""

N, M = map(int, input().split())

maps = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dir = {"U": 0, "D": 1, "L": 2, "R": 3}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
root = [[(i, j) for j in range(M)] for i in range(N)]


def find(x, y):
    if (x, y) == root[x][y]:
        return (x, y)
    root[x][y] = find(root[x][y][0], root[x][y][1])
    return root[x][y]


def union(A, B):
    A = find(A[0], A[1])
    B = find(B[0], B[1])

    if A != B:
        root[B[0]][B[1]] = A


def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


def dfs(x, y):
    direction = dir[maps[x][y]]
    visited[x][y] = True

    nextX, nextY = x + dx[direction], y + dy[direction]

    if checkBorder(nextX, nextY):
        if not visited[nextX][nextY]:
            union((nextX, nextY), (x, y))
            dfs(nextX, nextY)
        else:
            union((nextX, nextY), (x, y))

    return


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)

for i in range(N):
    for j in range(M):
        find(i, j)


case = {}

for i in range(N):
    for j in range(M):
        if str(root[i][j]) not in case:
            case[str(root[i][j])] = True

print(len(case))

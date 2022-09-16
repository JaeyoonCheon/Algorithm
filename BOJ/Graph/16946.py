"""
16946번 벽 부수고 이동하기 4

1.  처음 아이디어는 백트래킹을 이용한 dfs로 벽을 1->0->1로 바꿔가면서 가능한 연결된 그래프의 크기를 구해 출력했다.
    하지만 이 방법으로 시간초과가 발생했는데, 잘 생각해보면 O(N^2*M^2)의 시간복잡도가 필요할 수 있다.
    따라서 시간을 줄이기 위해 중복을 제거해야 했는데, 중복되는 부분은 동일한 0이 포함된 그래프를 벽을 만날 때 마다 계속 새로 방문하여
    그 개수를 구하는 것이었다.
    
2.  어떤 0이 속한 0으로만 구성된 그래프를 번호를 매겨놓고 그 번호와 그래프의 크기를 매칭시켜놓으면 나중에 벽을 만났을 때
    4번만 연산을 수행하면 해결할 수 있게 된다!
    우선, 초기 상태에서 방문하지 않은 0에 대해 dfs로 탐색 후 지난 경로에 번호를 매기고 총 크기를 따로 번호-크기로 저장해 놓았다.
    이후 벽을 깨고 이동할 경로를 구할 때 4방향에 대해 인접한 0의 번호와 매칭되는 크기를 결과에 더해주고, 이미 만난 번호(그래프가 여러 변에 인접)일 경우
    더해주지 않고 지나쳐야 한다. 이 방법으로는 결과값을 빠르게 구할 수 있었다.
    
3.  하지만, 파이썬 특성 상 재귀 단계는 기본 1000인데 최대로 필요한 재귀 깊이는 1000*1000이 될 것이다. 따라서 재귀를 이용한 dfs가 아닌
    큐를 이용한 bfs를 사용해 0의 그래프를 구해주어 해결했다.
"""

import sys, collections

N, M = map(int, input().split())

maps = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = []
usedBundles = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


def dfs_numbering(x, y, count, number):
    visited[x][y] = True
    cache[x][y] = number
    count += 1

    for i in range(4):
        if checkBorder(x + dx[i], y + dy[i]):
            if maps[x + dx[i]][y + dy[i]] == 0 and not visited[x + dx[i]][y + dy[i]]:
                count += dfs_numbering(x + dx[i], y + dy[i], 0, number)

    return count


def bfs_numbering(x, y, number):
    q = collections.deque()
    count = 0

    q.append((x, y))
    visited[x][y] = True
    cache[x][y] = number
    count += 1

    while q:
        curr = q.popleft()
        x, y = curr[0], curr[1]

        for i in range(4):
            if checkBorder(x + dx[i], y + dy[i]):
                if (
                    maps[x + dx[i]][y + dy[i]] == 0
                    and not visited[x + dx[i]][y + dy[i]]
                ):
                    q.append((x + dx[i], y + dy[i]))
                    visited[x + dx[i]][y + dy[i]] = True
                    cache[x + dx[i]][y + dy[i]] = number
                    count += 1

    return count


cache = [[-1 for _ in range(M)] for _ in range(N)]
bundles = [0] * (N * M)
result = [[0] * M for _ in range(N)]

num = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            if cache[i][j] == -1:
                # count = dfs_numbering(i, j, 0, num)
                count = bfs_numbering(i, j, num)
                bundles[num] = count
                num += 1
            else:
                continue


for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            usedBundles = []
            for dir in range(4):
                x, y = i + dx[dir], j + dy[dir]
                if checkBorder(x, y):
                    if maps[x][y] == 0 and cache[x][y] not in usedBundles:
                        visited[x][y] = True
                        result[i][j] += bundles[cache[x][y]]
                        usedBundles.append(cache[x][y])

            result[i][j] = (result[i][j] + 1) % 10


for i in range(N):
    for j in range(M):
        print(result[i][j], end="")
    print()

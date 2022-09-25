import sys, collections

sys.setrecursionlimit(50 * 60)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]


def solution(n, m, x, y, r, c, k):
    answer = []

    dir = {1: "d", 2: "l", 3: "r", 4: "u"}

    minPath = float("inf")

    maze = [["."] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    maze[x - 1][y - 1] = "S"
    maze[r - 1][c - 1] = "E"

    def checkBorder(x, y):
        nonlocal n, m

        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return True

    def findPath(x, y, count, path):
        nonlocal k, minPath

        if minPath:
            return

        visited[x][y] = True

        if maze[x][y] == "E":
            if count < k:
                for i in range(k - count):
                    path = path * 10 + 4
            minPath = path
            return
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if checkBorder(nx, ny) and not visited[x][y]:
                    if count < k:
                        visited[x][y] = True
                        newPath = path * 10 + (i + 1)
                        findPath(nx, ny, count + 1, newPath)

    def dfs(x, y, count, path):
        nonlocal k, minPath

        if count == k:
            if maze[x][y] == "E" and minPath > path:
                minPath = path
            return
        else:
            if minPath != float("inf"):
                tempPath = path * (10 ** (k - count))
                if tempPath > minPath:
                    return

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if checkBorder(nx, ny):
                    if count < k:
                        newPath = path * 10 + (i + 1)
                        dfs(nx, ny, count + 1, newPath)

    findPath(x - 1, y - 1, 0, 0)
    dfs(x - 1, y - 1, 0, 0)

    if minPath != float("inf"):
        while minPath:
            answer.append(dir[minPath % 10])
            minPath = minPath // 10

        answer.reverse()
        answer = "".join(answer)
    else:
        answer = "impossible"

    return answer


test1 = [3, 4, 2, 3, 3, 1, 5]
test3 = [50, 50, 1, 1, 50, 50, 2500]

print(solution(25, 25, 1, 1, 25, 25, 1250))

"""
3109번 빵집

1.  왼쪽의 시작 열에서 오른쪽의 도착 열까지 도착하는 파이프를 최대한 여러 개 까는 문제이다.
    이때 파이프는 우상, 우, 우하향 3가지 방향으로만 설치 가능하다. 만약 파이프를 가장 윗 행부터 깔아본다고 생각하면 공간을 생각해
    우상 -> 우 -> 우하 순서로 까는게 가장 효율적이라는 것을 직감적으로 알 수 있다. 따라서 이 문제는 그리디 + DFS를 적용하면 쉽게 해결 가능하다.
"""

import sys

R, C = map(int, input().split())

area = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dir = [-1, 0, 1]


def check(x, y):
    if x < 0 or x >= R or y < 0 or y >= C:
        return False
    return True


def dfs(x, y):
    installed = False

    if y == C - 1:
        visited[x][y] = True
        return True

    for i in range(3):
        dx = x + dir[i]
        dy = y + 1

        if check(dx, dy) and area[dx][dy] == "." and not visited[dx][dy]:
            if dfs(dx, dy):
                installed = True
                break

    if installed:
        visited[x][y] = True
        return True
    else:
        area[x][y] = "x"
        return False


count = 0

for block in range(R):
    result = dfs(block, 0)

    if result:
        count += 1

print(count)

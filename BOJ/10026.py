"""
10026번 적록색약
"""

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def dfs(x, y):
    
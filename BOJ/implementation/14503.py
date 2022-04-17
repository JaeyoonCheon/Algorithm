"""
14503번 로봇 청소기
"""

N, M = map(int, input().split())

r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

cleaned = [[False] * M for _ in range(N)]

cleaned[r][c] = True

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while True:
    if 
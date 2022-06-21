"""
2638번 치즈
"""
N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

air = [[False] * M for _ in range(N)]

visited = [[False] * M for _ in range(N)]


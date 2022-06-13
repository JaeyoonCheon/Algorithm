"""
2448번 별 찍기 11
"""

N = int(input())

paper = [[" "] * (2 * N - 1) for _ in range(N)]

step = 0
for i in range(N):
    for j in range(N - 1 - step, N + step):
        paper[i][j] = "*"
    step += 1

print()

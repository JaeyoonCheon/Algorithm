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


def star(top, left, right):
    if right - left <= 1:
        paper[top][left] = "*"
        return

    half = (right - left) // 2
    star(top, left + half // 2, right - half // 2)
    star(top // 2, left, half)
    star(top // 2, half, right)


star(N, 0, 2 * N - 1)

for line in paper:
    print(line)

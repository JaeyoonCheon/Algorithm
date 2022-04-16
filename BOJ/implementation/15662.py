"""
15662번 톱니바퀴 2
"""

T = int(input())

gear = [list(map(int, list(input()))) for _ in range(T)]

top = [0] * T

K = int(input())

operation = [list(map(int, input().split())) for _ in range(K)]

for iter in range(K):
    start = operation[iter][0] - 1
    direction = operation[iter][1]
    rotate = [0] * T

    tempDir = direction
    for i in range(start - 1, 0, -1):
        if gear[i + 1][(top[i + 1] - 2) % 8] != gear[i][(top[i] + 2) % 8]:
            rotate[i] = (top[i] + tempDir) % 8
        else:
            break
        tempDir *= -1

    tempDir = direction
    for i in range(start + 1, T):
        if gear[i - 1][(top[i - 1] + 2) % 8] != gear[i][(top[i] - 2) % 8]:
            rotate[i] = (top[i] + tempDir) % 8
        else:
            break
        tempDir *= -1

    rotate[start] += (-1 * direction) % 8

    for i in range(T):
        top[i] = rotate[i]

count = 0

for i in range(T):
    if gear[i][top[i]] == 1:
        count += 1

print(count)

"""
10830번 행렬 제곱

1.  일반적으로 모든 행렬을 B번 거듭제곱하면서 B승을 만드는것은 지수시간이 걸리므로 시간적 측면에서 아주 비효율적이다.

2.  따라서, 승을 절반으로 쪼개 재귀적으로 호출하여 곱하면 로그*N 시간이 걸리도록 만들 수 있다.
"""

import sys

MAX_SIZE = 100000001

N, B = map(int, input().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def multiply(A, B):
    C = [[1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += A[i][k] * B[k][j] % 1000
            C[i][j] = sum % 1000

    return C


def toPower(N):
    if N == 1:
        return matrix
    half = toPower(N // 2)
    if N % 2 == 0:
        return multiply(half, half)
    else:
        return multiply(multiply(half, matrix), half)


result = toPower(B)

for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=" ")
    print()

"""
11444번 피보나치 수 6

1.  피보나치 수를 구하기 위해 재귀/DP 등의 방법으로 풀이하였으나 이 문제에서는
    n이 아주 큰 수가 입력되므로 해당 방법을 사용할 수가 없다.
    
2.  피보나치의 일반항으로 해를 구하려 했으나 부동소수점 오차를 고려하지 못해
    값이 정확하게 구해지지 않는다.
    
3.  Fn = Fn_1 + Fn_2라는 식을 행렬로 표현해 거듭제곱법을 사용하여 해결할 수 있는 방법이 있으며
    이 방법은 logN 시간에 해결할 수 있다.
"""

import math, sys

sys.setrecursionlimit(100000)

N = int(input())
MOD = 1000000007

matrix = [[1, 1], [1, 0]]


def DP_optimized(N):
    first = 0
    second = 1
    next = 0

    for _ in range(3, N + 2):
        next = (first + second) % MOD
        first, second = second, next


def generalTerm(N):
    sqrt5 = decimal(math.sqrt(5))
    return (1 / sqrt5) * (pow((1 + sqrt5) / 2, N) - pow((1 - sqrt5) / 2, N))


def multiply(A, B):
    newMatrix = [[0, 0], [0, 0]]

    newMatrix[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    newMatrix[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    newMatrix[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    newMatrix[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD

    return newMatrix


def matrixPow(N, M):
    if N == 1:
        return M
    elif N % 2 == 0:
        partial = matrixPow(N // 2, M)
        return multiply(partial, partial)
    else:
        partial = matrixPow(N - 1, M)
        return multiply(partial, M)


if N == 1:
    print(1)
else:
    print(matrixPow(N - 1, matrix)[0][0] % MOD)

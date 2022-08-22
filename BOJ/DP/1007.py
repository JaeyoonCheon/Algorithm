"""
1007번 벡터 매칭
"""

import itertools, copy
from math import sqrt

T = int(input())

for _ in range(T):
    N = int(input())

    vectors = [list(map(int, input().split())) for _ in range(N)]

    total = [0, 0]

    for i in vectors:
        total[0] += i[0]
        total[1] += i[1]

    vectorsComb = list(itertools.combinations(vectors, N // 2))

    def vectorSize(vectorMatch):
        totalSum = copy.deepcopy(total)
        matchingSum = [0, 0]

        for i in vectorMatch:
            matchingSum[0] += i[0]
            matchingSum[1] += i[1]

        result = [totalSum[0] - matchingSum[0] * 2, totalSum[1] - matchingSum[1] * 2]

        return sqrt(result[0] ** 2 + result[1] ** 2)

    vectorMatchings = list(map(vectorSize, vectorsComb))

    print(min(vectorMatchings))

"""
1007번 벡터 매칭
"""

import itertools
from math import sqrt

T = int(input())

for _ in range(T):
    N = int(input())

    vertexs = [list(map(int, input().split())) for _ in range(N)]

    vertexsPerm = list(itertools.permutations(vertexs, 2))

    vectors = list(map(lambda x: (x[0][0] - x[1][0], x[0][1] - x[1][1]), vertexsPerm))

    vectorsComb = list(itertools.combinations(vectors, N // 2))

    def vectorSize(vectorMatch):
        totalVector = [0, 0]

        for v in vectorMatch:
            totalVector[0] += v[0]
            totalVector[1] += v[1]

        return sqrt(totalVector[0] ** 2 + totalVector[1] ** 2)

    vectorMatchings = list(map(vectorSize, vectorsComb))

    print(min(vectorMatchings))

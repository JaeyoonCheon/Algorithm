"""
10819번 차이를 최대로
"""

import itertools


def getSummation(N, seq):
    sum = 0
    for i in range(N - 1):
        sum += abs(seq[i] - seq[i + 1])

    return sum


def getMaxSum(N, numbers):
    partialMax = 0
    for i in itertools.permutations(numbers, N):
        sumVal = getSummation(N, i)
        if sumVal > partialMax:
            partialMax = sumVal

    print(partialMax)


N = int(input())
numbers = list(map(int, input().split()))

getMaxSum(N, numbers)

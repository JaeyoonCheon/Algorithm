"""
1920번 수 찾기

1.  기본적인 수 탐색 문제.
    최대 크기가 100000이고 정수의 크기가 INT 범위 내의 모든 수이기 때문에,
    기본적인 순차 탐색으로는 탐색 시 시간 초과가 우려되므로 이진 탐색을 적용하여 N -> logN 시간 복잡도를 적용
"""

import sys


def findNumber(A, num):
    global N

    lo, hi = 0, N - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if num == A[mid]:
            return True
        elif num < A[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return False


N = int(input())

A = list(map(int, sys.stdin.readline().split()))

M = int(input())

B = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in B:
    if findNumber(A, i):
        print(1)
    else:
        print(0)

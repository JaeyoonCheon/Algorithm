"""
2805번 나무 자르기

1.  일련의 나무들을 h만큼 잘라 잘린 부분의 합이 M보다 큰 최대의 h를 찾는 문제.

2.  첫번째 시도로 가장 높은 나무의 높이부터 1씩 내려오면서 자를 수 있는 최대의 높이를
    구하려고 시도하였다.
    이 경우, 나무의 수가 백만개이기 때문에 시간 초과가 발생한다.
    
3.  이 문제에서 구하려는 값은 최대의 높이이므로, 최적화 방법을 적용할 수 있고 가장 쉬운 이분 탐색을 적용하였다.
    나무의 최대 높이와 바닥 사이에서 잘랐을 때 M이 되는 지점을 찾으면 그 지점이 최대 높이가 될 것이다.
"""

import sys


def findHeight(trees, N, M, hi, lo):
    candidate = []
    while lo + 1 < hi:
        mid = (hi + lo) // 2
        sum = 0

        for j in trees:
            diff = j - mid
            if diff < 0:
                continue
            sum += diff

        if sum >= M:
            lo = mid
        else:
            hi = mid

    return lo


N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

hi = max(trees) + 1
lo = 0

print(findHeight(trees, N, M, hi, lo))

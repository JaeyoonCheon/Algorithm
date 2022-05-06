"""
2839번 설탕 배달

1.  DP 이용하여 최소값 탐색하는 문제.

2.  정수론을 활용, -(n in[4,7])or n-2*n//5*2 식을 세워 풀이해도 통과함
    n = 5a+3b라고 할 때, a는 3kg 봉투의 개수, b는 5kg 봉투의 개수
    n에 대입 후 위 식을 풀이하면 a+b, 즉 필요한 봉투의 개수가 나온다.
"""

import sys

sys.setrecursionlimit(2500)
MAX_SUGAR_WEIGHT = 5001

cache = [False] * MAX_SUGAR_WEIGHT


def delivery(sugar):
    if cache[sugar]:
        return cache[sugar]

    if sugar == 0:
        return 0
    elif sugar < 0:
        return MAX_SUGAR_WEIGHT
    else:
        cache[sugar] = min(delivery(sugar - 3), delivery(sugar - 5)) + 1
        return cache[sugar]


N = int(input())
minCount = delivery(N)

if minCount > MAX_SUGAR_WEIGHT:
    print(-1)
else:
    print(minCount)

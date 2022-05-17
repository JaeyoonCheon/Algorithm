"""
1764번 듣보잡

1.  듣지 못하는 집합과 보지 못하는 집합 간의 교집합을 구하는 set 자료구조 응용 문제
"""

import sys

N, M = map(int, input().split())

listen = set([sys.stdin.readline().rstrip() for _ in range(N)])
look = set([sys.stdin.readline().rstrip() for _ in range(M)])

listenAndLook = listen & look

print(len(listenAndLook))

sortedListenAndLook = sorted(listenAndLook)

for item in sortedListenAndLook:
    print(item)

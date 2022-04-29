"""
2164번 카드2

1.  기본적인 큐 응용 문제
"""

import collections

N = int(input())

q = collections.deque()

for i in range(1, N + 1):
    q.appendleft(i)

while True:
    first = q.pop()
    if not q:
        print(first)
        break
    second = q.pop()
    if not q:
        print(second)
        break
    q.appendleft(second)

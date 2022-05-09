"""
10773번 제로

1.  스택 사용 / 합의 삽입 시 마다의 계산
"""

import sys
import collections

K = int(sys.stdin.readline())
stack = collections.deque()
sum = 0

for _ in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.appendleft(num)
        sum += num
    else:
        lastest = stack.popleft()
        sum -= lastest

print(sum)

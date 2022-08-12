"""
12015번 가장 긴 증가하는 부분 수열 2

1.  LIS의 길이를 구하는 문제.
    주어지는 수열의 길이가 백만까지이므로, 단순 DP를 통한 LIS의 길이는 구하는 방법은
    O(N^2)가 걸리므로 사용하기 힘들다.
"""

import sys, bisect

N = int(input())

seq = list(map(int, sys.stdin.readline().split()))

cache = [float('inf')]*(N+1)
cache[0], cache[1] = -float('inf'), seq[0]

currMax = 1

for num in seq:
    if cache[currMax] >= num:
        nextIdx = bisect.bisect_left(cache, num)
        cache[nextIdx] = num
    else:
        currMax += 1
        cache[currMax] = num
        
print(currMax)
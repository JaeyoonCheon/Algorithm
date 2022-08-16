"""
12015번 가장 긴 증가하는 부분 수열 2

1.  LIS의 길이를 구하는 문제.
    주어지는 수열의 길이가 백만까지이므로, 단순 DP를 통한 LIS의 길이는 구하는 방법은
    O(N^2)가 걸리므로 사용하기 힘들다.
    
2.  DP 사용 시 N^2의 시간복잡도를 줄이기 위한 방안 중의 하나로 이진 탐색을 사용해 N loop를 logN loop만에 탐색하도록 조정하는 것이다.
    https://shoark7.github.io/programming/algorithm/3-LIS-algorithms#5 포스팅의 5-1 문단을 참고하여 풀이했다.
    
"""

import sys, bisect

N = int(input())

seq = list(map(int, sys.stdin.readline().split()))

cache = [float("inf")] * (N + 1)
cache[0], cache[1] = -float("inf"), seq[0]

currMax = 1

for num in seq:
    if cache[currMax] >= num:
        nextIdx = bisect.bisect_left(cache, num)
        cache[nextIdx] = num
    else:
        currMax += 1
        cache[currMax] = num

print(currMax)

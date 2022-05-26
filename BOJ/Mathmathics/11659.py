"""
11659번 구간 합 구하기 4

1.  초기 시도에서는 주어진 수들을 받아 구간마다 순차적으로 합을 구해 출력했으나
    당연하게도 최악의 경우 O(N^2) 시간이기 때문에 시간 안에 해결할 수 없다.
    
2.  어떤 구간의 합을 구하기 위해, 주어지는 숫자를 입력받을 때 마다 각기의 누적 합을 저장해 놓고
    구간의 시작까지의 누적합을 구간의 끝까지의 누적합에서 빼 준다면 그 사이 구간의 누적 합이 구해진다.
"""

import sys

N, M = map(int, input().split())

numbers = list(map(int, sys.stdin.readline().split()))

accumualatedSum = [0]

sum = 0
for i in numbers:
    sum += i
    accumualatedSum.append(sum)

for _ in range(M):
    start, end = map(int, input().split())

    sum = accumualatedSum[end] - accumualatedSum[start - 1]

    print(sum)

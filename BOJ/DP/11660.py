"""
11660번 구간 합 구하기 5

1.  구간 합을 구하는 문제 중 2차원으로 생각해 보아야 할 문제이다.

2.  일차원 배열에서 구간 합을 구할 때, 미리 처음부터 계산된 누적 합을 저장하는
    배열을 따로 만들었다. 이 문제에서도 유사하게 해당 방법을 적용한다.
    
3.  (x1, y1)에서 (x2, y2)까지의 구간 합은 x1 ~ x2 사이의 행에서
    y1 ~ y2 사이의 값들을 모두 더한 값들을 모두 더한 것이다.
    따라서, 각 행마다의 누적 합 배열을 계산하여 이차원 배열로 저장한 뒤,
    행마다 y2까지의 누적합 - y1까지의 누적합 + (포함 구간이므로) y1위치의 값을 계산하여
    모두 더해주면 된다.
"""

import sys

N, M = map(int, input().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
prefixSum = [[0] * N for _ in range(N)]

for i in range(N):
    sum = 0
    for j in range(N):
        sum += table[i][j]
        prefixSum[i][j] = sum

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    sum = 0

    for i in range(x1 - 1, x2):
        sum += prefixSum[i][y2 - 1] - prefixSum[i][y1 - 1] + table[i][y1 - 1]

    print(sum)

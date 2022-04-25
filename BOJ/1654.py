"""
1654번 랜선 자르기

1.  처음 시도
    단순히 1~가장 큰 랜선의 길이 사이에서
    모든 랜선을 선택한 길이로 나눈 몫의 합이 N보다 커지는 경우에서
    길이의 최대값을 순차적으로 구했다.
    이 경우, 범위 1~2^31-1 에서 시간제한 2초 안에 도저히 해결 불가능했다.
    
2.  문제 분석
    결과적으로, 순차적으로 모든 길이에 대해 개수를 탐색하는 것이 아닌
    이분 탐색으로 N을 logN으로 시간 복잡도를 줄여 계산해 본다.
    
3.  Binary Search
    생각한 알고리즘은 어떤 선택한 길이가 N보다 많은 몫을 만들어내는 케이스에서
    최대 길이를 구해야 하는 것이므로 while을 탈출 시켜 구해진 lo값에서 -1을 더해주면
    구하려는 mid값이 도출
"""

import sys

K, N = map(int, sys.stdin.readline().split())

line = [int(input()) for _ in range(K)]

lo = 1
hi = max(line) + 1

while lo < hi:
    mid = (lo + hi) // 2
    number = 0

    for i in line:
        number += i // mid

    # 개수를 충족하지 못하면 mid 보다 작은 길이에서 찾아야 한다.
    if number < N:
        hi = mid
    # 만들 수 있는 개수가 N보다 같거나 많을 경우 길이를 늘려봐도 된다.
    else:
        lo = mid + 1

print(lo - 1)

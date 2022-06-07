"""
9465번 스티커

1.  처음에는 접근 방식을 헤맸으나 2xN 형식으로 입력되는 스티커 판에
    스티커 합계의 최대값을 구하는 문제로 파악하면 DP로 접근해야겠닥는 생각이 듬
    
2.  주어진 2xN 스티커판을 처음부터 열 방향으로 계산할 수 있었다.
    1)  0열은 주어진 스티커를 선택하면 최대값이다.
    2)  1열은 0열의 교차되는 위치의 스티커와 현재 스티커의 합이 최대값이다.
    3)  1~N-1 열은 1열 전의 교차되는 위치의 스티커, 2열 전의 두 스티커,
        총 3개의 스티커가 변을 공유하지 않고 영향받지 않는 스티커이므로
        3개의 스티커의 누적 합 중 가장 큰 것을 선택하여 현재 스티커를 더한 것이 최대값이다.
"""

import sys

T = int(input())

for _ in range(T):
    N = int(input())

    stickers = []

    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))

    DP = [[0, 0] for _ in range(N)]

    DP[0][0], DP[0][1] = stickers[0][0], stickers[1][0]

    for i in range(1, N):
        for j in range(2):
            if i == 1:
                DP[i][j] = DP[i - 1][(j + 1) % 2] + stickers[j][i]
            else:
                DP[i][j] = max(
                    DP[i - 1][(j + 1) % 2] + stickers[j][i],
                    DP[i - 2][j % 2] + stickers[j][i],
                    DP[i - 2][(j + 1) % 2] + stickers[j][i],
                )

    maxVal = 0

    for i in DP:
        if maxVal < max(i):
            maxVal = max(i)

    print(maxVal)

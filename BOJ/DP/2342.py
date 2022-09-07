"""
2342번 Dance Dance Revolution

1.  접근이 힘든 문제였다. 처음에는 단순히 4방향을 향하는 두 발을 최소 거리로 움직일 수
    있는 발을 우선으로 각 지시마다의 최단 거리를 구하려고 했으나, 풀다 보니 짧은 경우의 수에서는
    맞아 떨어질 수도 있으나 지시가 많아질 수록 발의 이전 위치를 나타내는 경우의 수가 많아져
    모든 경우를 따져야 하는데 이 방법으로는 무리였다.
    
2.  따라서, 아래쪽 주석처리한 코드를 보면 Top-down 방식의 DP를 사용해
    DP[현재 지시 번호][왼발 위치][오른발 위치] 
    = min(
        DP[이후 지시 번호][왼발의 위치][오른발이 지시번호] + 오른발이 현재의 위치에서 지시번호로 이동하는 cost,
        DP[이후 지시 번호][왼발이 지시번호][오른발의 위치] + 왼발이 현재의 위치에서 지시번호로 이동하는 cost
        )
    의 점화식으로 나타낼 수 있고 DP[0][0][0]을 밟으면 최종 cost를 구할 수 있을 것이라고 생각했다.
    하지만 답은 맞았으나 파이썬 pypy3에서 100000번 재귀를 들어가다보니 메모리 초과가 발생하여
    iteration 방식의 Bottom-up 방식의 DP를 사용해야만 했다.
"""

import sys


def getDist(_from, _to):
    if _to == 0:
        if _from == 0:
            return 0
        return 2
    elif _from == _to:
        return 1
    elif abs(_from - _to) % 2 == 1:
        return 3
    else:
        return 4


inst = list(map(int, sys.stdin.readline().split()))
inst.pop()

length = len(inst)

if length == 0:
    print(0)
    sys.exit()

dp = [[[float("inf") for _ in range(5)] for _ in range(5)] for _ in range(length + 1)]
dp[-1][0][0] = 0

for i in range(length):
    for right in range(5):
        for left_prev in range(5):
            cost = getDist(inst[i], left_prev)
            dp[i][inst[i]][right] = min(
                dp[i][inst[i]][right], dp[i - 1][left_prev][right] + cost
            )

    for left in range(5):
        for right_prev in range(5):
            cost = getDist(inst[i], right_prev)
            dp[i][left][inst[i]] = min(
                dp[i][left][inst[i]], dp[i - 1][left][right_prev] + cost
            )

minCost = float("inf")

for i in range(5):
    for j in range(5):
        minCost = min(minCost, dp[length - 1][i][j])

print(minCost)

""" sys.setrecursionlimit(100000)


def getDist(_from, _to):
    if _from == _to:
        return 1
    elif _from == 0:
        return 2
    elif _from % _to == 1:
        return 3
    else:
        return 4


def find(step, left, right):
    global dp

    if step == len(inst) - 1:
        return 0
    if dp[step][left][right] != -1:
        return dp[step][left][right]

    dp[step][left][right] = min(
        find(step + 1, left, inst[step]) + getDist(right, inst[step]),
        find(step + 1, inst[step], right) + getDist(left, inst[step]),
    )
    return dp[step][left][right]


inst = list(map(int, sys.stdin.readline().split()))

dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]

print(find(0, 0, 0)) """

"""
7579번 앱

1.  이 문제에서의 메모리공간-비용은 곧 0/1 knapsack문제의 배낭 무게-가치와 유사하다.
    하지만 배낭문제와 달리 어떤 가능한 공간 내의 최대 가치를 찾는 것이 아니라 확보하기 위한 메모리 이상에서 소요되는 비용의 최소치를 찾는 문제로
    조건 설정을 달리 해야됨을 알 수 있으며, 메모리의 크기가 천만이므로 일반적인 배낭문제의 DP 해법으로는 메모리 초과가 발생할 우려가 높다.
    
2.  따라서 종료할 앱의 개수에 대한 메모리 공간 별 최소 비용을 구하는 것이 아닌
    종료할 앱의 개수에 대한 비용 별 확보 가능한 최대 메모리를 DP로 찾아 올라가면 앱 개수 당 100*100의 범위에서 찾아 낼 수 있다.

3.  dp[item][cost]는 item까지의 앱들을 가지고 cost의 비용이 들 경우 확보 할 수 있는 최대의 메모리 크기이다.
    0 ~ 주어진 비용의 합 maxCost까지 확인하면서 가능한 비용 cost에 대해,
    1)  현재 선택한 item의 비용이 가능한 비용 cost보다 작다면 현재 item-cost dp[item][cost]의 최대 메모리 크기와 
        item이 제외되었다고 간주하여 item-1, cost-costs[item]에 현재 item의 메모리를 더한 dp[item-1][cost-costs[item]]+app[item] 중 
        더 큰것을 선택
    2)  이후, 현재 비용에서 현재 선택한 item의 유무에 대한 비교를 하기 위해
        dp[item][cost], dp[item - 1][cost] 중 더 큰 것을 선택
"""

import sys

N, M = map(int, input().split())

app = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))


def findMinCost():
    maxCost = sum(cost)
    dp = [[0] * (maxCost + 1) for _ in range(N)]

    for item in range(N):
        for cost in range(maxCost + 1):
            if cost - costs[item] >= 0:
                dp[item][cost] = max(
                    dp[item][cost], dp[item - 1][cost - costs[item]] + app[item]
                )
            dp[item][cost] = max(dp[item][cost], dp[item - 1][cost])

    for i, c in enumerate(dp[N - 1]):
        if c >= M:
            return i

    return maxCost


print(findMinCost())

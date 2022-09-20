"""
RGB거리 2

1.  N까지의 x번 집일 때 3가지 색 중 하나를 택할 때의 최소값을 저장해 누적 합을 사용하는
    DP문제이다.
    
2.  RGB거리 1 문제에서 거의 유사한 문제를 풀이했었는데, 해당 문제에서는 첫 집과 끝 집이 연관되지 않았으나,
    이번 문제에서는 모든 집이 앞-뒤 집과 연관되어 같은 색이면 안되도록 해야 했다.
    
3.  따라서, 첫 집의 각 색마다 끝 집이 될 수 있는 2가지 색의 경우에서 최소값을 따로 계산해 저장해 놓으면된다.
    즉, 1번 집~N-2번 집까지는 동일한 점화식을 적용하는데 0번 집과 N-1번 집을 경우의 수를 쪼개 고려하면 되는 문제이다.
"""

import sys

N = int(input())

costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = [0] * 3

for color in range(3):
    cache = [[0, 0, 0] for _ in range(N)]

    cache[0][color] = costs[0][color]
    cache[0][(color + 1) % 3] = float("inf")
    cache[0][(color + 2) % 3] = float("inf")

    for i in range(1, N):
        for j in range(3):
            cache[i][j % 3] = (
                min(cache[i - 1][(j + 1) % 3], cache[i - 1][(j + 2) % 3])
                + costs[i][j % 3]
            )

    result[color] += min(cache[N - 1][(color + 1) % 3], cache[N - 1][(color + 2) % 3])

print(min(result))

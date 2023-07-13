"""

"""


T = int(input())

for testcase in range(T):
    N, M = map(int, input().split())

    INF = float("inf")

    minimum = INF

    G = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        X, Y, C = map(int, input().split())

        G[X][Y] = C

    for i in range(1, N + 1):
        minimum = min(minimum, G[i][i])
        G[i][i] = INF

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if k == i:
                continue
            for j in range(1, N + 1):
                if k == j:
                    continue
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]

    for i in range(1, N + 1):
        minimum = min(minimum, G[i][i])
        G[i][i] = INF

    print(f"#{testcase+1} " + minimum)

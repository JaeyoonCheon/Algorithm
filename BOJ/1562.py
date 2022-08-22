"""
1562번 계단 수
"""

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]
checking = [[[False for _ in range(10)] for _ in range(10)] for _ in range(N + 1)]

for i in range(10):
    if i == 0:
        continue
    checking[1][i][i] = True

for length in range(2, N + 1):
    for end in range(10):
        if end == 0:
            for i in range(10):
                if checking[length - 1][end + 1][i]:
                    checking[length][end][i] = True
            checking[length][end][end] = True

            if length == 10 and False not in checking[length][end]:
                dp[length][end] = 1
            elif length >= 10 and False not in checking[length][end]:
                dp[length][end] = dp[length - 1][end + 1]
        elif end == 9:
            for i in range(10):
                if checking[length - 1][end - 1][i]:
                    checking[length][end][i] = True
            checking[length][end][end] = True

            if length == 10 and False not in checking[length][end]:
                dp[length][end] = 1
            elif length >= 10 and False not in checking[length][end]:
                dp[length][end] = dp[length - 1][end - 1]
        else:
            for i in range(10):
                if checking[length - 1][end - 1][i] or checking[length - 1][end + 1][i]:
                    checking[length][end][i] = True
            checking[length][end][end] = True

            if length == 10 and False not in checking[length][end]:
                dp[length][end] = 1
            elif length >= 10 and False not in checking[length][end]:
                dp[length][end] = dp[length - 1][end - 1] + dp[length - 1][end + 1]

total = 0

for i in range(1, N + 1):
    for j in range(10):
        if False not in checking[i][j]:
            total += dp[i][j]

print(total)

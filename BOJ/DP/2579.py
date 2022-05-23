"""
2579번 계단 오르기

1.  간단한 DP 문제.

2.  계단은 1칸 뒤에서 올라오는 경우와 2칸 뒤에서 올라오는 경우로 나뉜다.
    1칸 뒤에서 올라올 때는 그 계단이 이전에 2칸 뒤에서 올라왔어야 하며,
    2칸 뒤에서 올라올 때는 그 계단이 1칸 뒤/2칸 뒤 어디서 올라왔는지 무관하게
    최대값을 고려한다.

3.  단계 별 점화식을 세우기 위해 필요한 초기 조건은
    dp[0][0], dp[0][1] = stairs[0], stairs[0]
    dp[1][0], dp[1][1] = stairs[0] + stairs[1], stairs[1]

4.  따라서, 점화식은
    dp[i][0] = dp[i - 1][1] + stairs[i]
    dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + stairs[i]
    (2 <= i < N)
"""

N = int(input())

stairs = [int(input()) for _ in range(N)]

dp = [[0, 0] for _ in range(N)]

dp[0][0], dp[0][1] = stairs[0], stairs[0]

if N > 1:
    dp[1][0], dp[1][1] = stairs[0] + stairs[1], stairs[1]

    for i in range(2, N):
        dp[i][0] = dp[i - 1][1] + stairs[i]
        dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + stairs[i]

print(max(dp[-1]))

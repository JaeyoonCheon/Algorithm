"""
1562번 계단 수

1.  문제의 개념에서 DP가 필요하다는 것은 염두에 두고 풀이를 했는데 처음에는 i길이에서 j로 끝나는 수열이 0~9 중의 수를 가질 경우를 구하려고 했다.
    하지만 이 부분에서 부족했던 점은 i길이에서 j로 끝나는 수열까지는 생각을 했는데 그 수열이 단순 10가지 0~9의 수를 가질 때의 경우의 수를 구하려고 하다보니
    모든 경우의 수를 체크하지 못했다는 점이다.
    
2.  i길이에서 j로 끝나는 수열의 경우, 수를 가질 수 있는 경우가 10가지가 아닌 (2^ 10)-1, 즉 1023가지의 경우의 수를 가질 수 있다!
    이것은 비트마스킹을 이용한 집합계산을 거치면 계산이 간단해진다.
    끝이 0인 경우 길이가 1 짧은 수열에서 9로 끝나는 수열의 경우의 수를 더할 수 없으며 끝이 9인 경우 길이가 1 짧은 수열에서 10으로 끝나는 수열의 경우의 수를
    더할 수 없다. 이 예외사항만 적용시켜 점화식을 구성해 주면 결과값을 구할 수 있다.
"""

N = int(input())

MARK = 1 << 10
MOD = 1000000000

checking = [[[0 for _ in range(MARK)] for _ in range(10)] for _ in range(N + 1)]

for i in range(10):
    if i == 0:
        continue
    checking[1][i][1 << i] = 1

for length in range(2, N + 1):
    for end in range(10):
        for check in range(MARK):
            bitmask = check | (1 << end)
            if end > 0:
                checking[length][end][bitmask] = (
                    checking[length][end][bitmask]
                    + checking[length - 1][end - 1][check]
                ) % MOD
            if end < 9:
                checking[length][end][bitmask] = (
                    checking[length][end][bitmask]
                    + checking[length - 1][end + 1][check]
                ) % MOD

            checking[length][end][bitmask] %= MOD

total = 0

for end in range(10):
    total = (total + checking[N][end][MARK - 1]) % MOD

print(total)

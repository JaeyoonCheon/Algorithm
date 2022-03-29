"""
11057번 오르막 수

1.  부분 단위 cache[i][j]는 i자리 수의 i번째 위치에 올 수 있는 수 j에 대해 만들 수 있는
    오르막 수의 갯수
"""

N = int(input())

cache = [[0] * 10 for _ in range(N)]

for i in range(10):
    cache[0][i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(j + 1):
            cache[i][j] += cache[i - 1][k]
        cache[i][j] %= 10007

print(sum(cache[N - 1]) % 10007)

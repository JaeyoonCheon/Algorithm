"""
10844번 쉬운 계단 수

1.  활용할 단위 조각 : i번째 자리에서 j 라는 수가 위치하면 그 아래자리 수들로
    만들 수 있는 모든 계단 수의 수
    
2.  우선,  0의 자리에서는 모두 0, 1의 자리인 1~9의 수에서는 계단 수를 각각의 수마다 1개로 간주

3.  이후 2~N 자리에서는 수를 고를 때 마다 계단 수로 만들 수 있는 경우가 1 아래, 1 위로 2개씩 나오게 된다.
    따라서, 2~N자리에 들어올 수 있는 0~9의 수는 이전 자리수의 j-1, j+1로 만들 수 있는 모든 계단 수의 합이 된다.
    결과적으로 기본 점화식은 cache[i][j] = cache[i-1][j-1] + cache[i-1][j+1]이 될 것이다.
    
4.  문제에서 주어지는 제약사항으로, '계단 수'라는 것의 정의로 인해 0은 1만 계단수로 가질 수 있으며
    9는 8만을 계단수로 가질 수 있다. 또한 가장 앞 자리가 0인 경우를 고려하지 않으므로 이 경우들을 모두
    제해주면 결과값을 구할 수 있다.
"""

modular = 1000000000
N = int(input())

cache = [[0] * 10 for _ in range(N + 1)]

for i in range(10):
    cache[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            if i == N:
                continue
            cache[i][j] = cache[i - 1][j + 1] % modular
            continue
        if j == 9:
            cache[i][j] = cache[i - 1][j - 1] % modular
            continue
        cache[i][j] = (cache[i - 1][j - 1] + cache[i - 1][j + 1]) % modular

cache[1][0] = 0
print(sum(cache[N]) % modular)

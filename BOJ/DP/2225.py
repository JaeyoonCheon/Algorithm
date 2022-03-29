"""
2225번 합분해

1.  cache[N][K]는 N개의 숫자 중 K개를 뽑아 합해 N을 만드는 경우의 수(중복/순서o)

2.  예를 들어, N은 x+x+a로 나타 낼 수 있는데, N에서 a를 빼면 남은 수는
    K-1개의 수로 N-a를 나타내어야 하는데 이것을 표현하면 cache[K-1][N-a]가 된다.
    이때 a는 0~N사이의 수이므로, cache[K][N]을 분해하면
    cache[K-1][N-0] + ... + cache[K-1][N-N]까지의 합으로 나타낼 수 있다.
    
3.  이것을 구현하기 위해서는 bottom-up에서 k, n, a를 loop해야 하므로 3번의 loop를 거치게 되어
    시간 복잡도가 N^3이 될 것이다.
    
4.  표를 그려 살펴보면, 2차원 상의 배열에서 위와 같이 cache[K-1][N-0] + ... + cache[K-1][N-N]의 값을
    cache[K][N-1]에 저장되어 있다는 것을 발견 할 수 있으므로, 점화식을 요약 가능하다.
    
5.  결과적으로, 이 문제를 다르게 생각하면, N개 중 K개를 중복을 포함하여 순서있게 뽑는 중복 순열과 같아진다.
    N_H_K로, 순열로 표현하면 (N+K-1)_P_K가 된다.
"""

N, K = map(int, input().split())

cache = [[0] * (N + K + 1) for _ in range(N + K + 1)]

cache[1][0] = cache[1][1] = 1

for i in range(2, N + K):
    cache[i][0] = 1
    for j in range(1, K + 1):
        cache[i][j] = (cache[i - 1][j - 1] + cache[i - 1][j]) % 1000000000

print(cache[N + K - 1][K - 1] % 1000000000)

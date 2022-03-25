"""
15990번 1, 2, 3 더하기 5

1.  점화식을 찾는 것이 어려운 문제.

2.  우선, 가장 기초적인 1, 2, 3으로 수를 표현하는 방법은
    cache[N] = cache[N-1] + cache[N-2] + cache[N-3]으로 나타나진다.
    곧, 1과 N-1을 1/2/3으로 만드는 갯수 + 2와 N-2을 1/2/3으로 만드는 갯수 + 3과 N-3을 1/2/3으로 만드는 갯수
    를 의미하며 별도의 제약은 없으므로 단순한 DP를 사용하면 된다.
    
3.  이 문제에서는 특별히, 같은 수를 두 번 이상 연속해서 사용하면 안된다라는 제약이 존재하므로,
    점화식을 구성할 때 각각의 경우마다 제약조건을 피해 나누어서 생각해야 한다.
    1) 1을 선택하면 N-1을 1이 아닌 2,3으로만 만들어야 하므로,
    n, 1 -> n-1, 2 + n-1, 3
    2) 2를 선택하면 N-2를 2가 아닌 1,3으로만 만들어야 하므로,
    n, 2 -> n-2, 1 + n-2, 3
    1) 3을 선택하면 N-3을 3이 아닌 1,2으로만 만들어야 하므로,
    n, 3 -> n-3, 1 + n-3, 2
    
    각 경우의 점화식은
    1) cache[n][1] = cache[n - 1][2] + cache[n - 1][3]
    2) cache[n][2] = cache[n - 2][1] + cache[n - 2][3]
    3) cache[n][3] = cache[n - 3][1] + cache[n - 3][2]

    이 때, 경우의 수가 매우 커질 수 있으므로, 분배법칙이 가능한 MOD 연산을 각각의 점화식에 적용
"""

T = int(input())

forfind = []
for _ in range(T):
    forfind.append(int(input()))

cache = [[0] * 4 for _ in range(max(forfind) + 1)]

cache[1][1] = cache[2][2] = cache[3][1] = cache[3][2] = cache[3][3] = 1

for i in range(4, max(forfind) + 1):
    cache[i][1] = (cache[i - 1][2] + cache[i - 1][3]) % 1000000009
    cache[i][2] = (cache[i - 2][1] + cache[i - 2][3]) % 1000000009
    cache[i][3] = (cache[i - 3][1] + cache[i - 3][2]) % 1000000009

for i in forfind:
    print((cache[i][1] + cache[i][2] + cache[i][3]) % 1000000009)

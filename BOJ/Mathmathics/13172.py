"""
13172번 Σ

1.  정수론 - 페르마의 소정리를 응용한 문제.

2.  여러 개의 주사위의 기대값의 합을 기약분수로 나타낸 후,
    페르마의 소정리를 사용해 모듈러 역원을 구하고 그것으로 기약분수의 정보를 가지는 수를 만들 수 있다.
"""

MOD = 1000000007

M = int(input())


def GCM(num):
    A, B = num[0], num[1]

    while B != 0:
        R = A % B
        A = B
        B = R
    return A


curr = [0, 1]

for _ in range(M):
    S, N = map(int, input().split())

    curr[0] = curr[0] * S + N * curr[1]
    curr[1] = curr[1] * S

    div = GCM(curr)

    curr[0] = (curr[0] // div) % MOD
    curr[1] = (curr[1] // div) % MOD


print((curr[0] * pow(curr[1], MOD - 2, MOD)) % MOD)

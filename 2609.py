"""
2609번 최대공약수와 최소공배수

1.  최대공약수를 구하기 위해 유클리드 호제법을 이용
    * 유클리드 호제법:
        GCD(A, B) = GCD(B, A%B)

2.  최소공배수는 각 수를 최대공약수로 나눈 것의 곱에 최대공약수를 곱한 것
"""

N, M = map(int, input().split())


def getGCD(N, M):
    A = B = 0
    if N > M:
        A = N
        B = M
    else:
        A = M
        B = N

    while True:
        C = A % B
        if C == 0:
            break
        A = B
        B = C

    return B


gcd = getGCD(N, M)

print(gcd)
print(gcd * (N // gcd) * (M // gcd))

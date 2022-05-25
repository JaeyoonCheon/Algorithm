"""
9461번 파도반 수열

1.  심플한 DP문제.

2.  P[i] = P[i - 2] + P[i - 3]의 점화식을 빠르게 찾는 것이 관건.
"""

T = int(input())

for _ in range(T):
    P = [0] * 101

    P[1], P[2], P[3] = 1, 1, 1

    N = int(input())

    if N > 3:
        for i in range(4, N + 1):
            P[i] = P[i - 2] + P[i - 3]

    print(P[N])

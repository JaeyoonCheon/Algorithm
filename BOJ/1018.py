"""
1018번 체스판 다시 칠하기
"""

N, M = map(int, input().split())

min = N * M

for i in range(N - 8):
    for j in range(M - 8):
        val = check(i, j)
        if val < min:
            min = val

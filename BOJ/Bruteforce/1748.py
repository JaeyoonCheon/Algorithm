"""
1748번 수 이어 쓰기 1
"""


def getDigit(N):
    length = 0

    while True:
        N = int(N / 10)
        length += 1
        if N == 0:
            break

    return length


def findLength(N):
    length = 0
    digit = getDigit(N)

    for i in range(1, digit):
        length += 9 * pow(10, i - 1) * i

    length += (N - pow(10, digit - 1) + 1) * digit

    return length


N = int(input())

print(findLength(N))

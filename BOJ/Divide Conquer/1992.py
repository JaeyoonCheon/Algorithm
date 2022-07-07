"""
1992번 쿼드트리

1.  기본적인 재귀 - 분할정복 문제.

2.  다만 이 문제에서는 각 재귀 단계에서 처리한 문자열을
    반환하여 하나의 문자열로 압축해야 하고,
    합칠 때의 순서가 중요하다.
"""

N = int(input())

frame = [list(input()) for _ in range(N)]


def compression(x, y, length):
    color = frame[x][y]
    isSame = True

    if length == 1:
        return color

    for i in range(x, x + length):
        for j in range(y, y + length):
            if frame[i][j] != color:
                isSame = False

    if isSame:
        return color
    else:
        return (
            "("
            + compression(x, y, length // 2)
            + compression(x, y + length // 2, length // 2)
            + compression(x + length // 2, y, length // 2)
            + compression(x + length // 2, y + length // 2, length // 2)
            + ")"
        )


print(compression(0, 0, N))

"""
1074번 Z

1.  문제에서 제시하는 Z모양은 최소 단위가 2x2 정사각형에서 발생하고,
    2^N 길이의 정사각형을 4분할한 것에 대해 반복적으로 수행되고 있는 것을 알 수 있다.
    따라서, 가장 큰 곳부터 시작하여 4-1-2-3 사분면 순서대로 좌표를 넘기고
    수행하는 길이를 절반으로 줄여 길이가 2가 되면 숫자를 기록하는 방식으로 풀이하였다.
"""

N, R, C = map(int, input().split())

board = [[0] * 2 ** N for _ in range(2 ** N)]

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

count = 0


def write(length, x, y):
    global count
    if length == 2:
        for i in range(4):
            board[x + dx[i]][y + dy[i]] = count
            count += 1
        return
    else:
        for i in range(4):
            write(
                length // 2,
                x + dx[i] * length // 2,
                y + dy[i] * length // 2,
            )
    return


write(2 ** N, 0, 0)

print(board[R][C])

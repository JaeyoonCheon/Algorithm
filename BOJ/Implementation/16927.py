"""
16927번 배열 돌리기 2

1.  배열 돌리기 1 문제보다 회전 횟수의 상한이 1000배 증가하였다.
    따라서, 시간 제한을 지키기 위해 중복되어 무의미한 회전 횟수를 줄여야 한다.
    
2.  처음에는 모든 각각의 회전 그룹의 원 위치로 돌아오는 회전 횟수의 최소 공배수를 구하여
    주어진 회전 횟수 R에 mod 연산을 하여 회전 횟수를 줄여보았다.
    그러나 이 방법으로도 시간초과가 발생하였다.
    
3.  따라서, 이 이상으로 회전 횟수를 줄이기 위해서는 각각의 그룹에 별도로 mod 연산을 취하여
    무의미한 회전 횟수를 줄이는 방법을 선택하였다.
    각 그룹이 회전하여 다시 원 위치로 복귀하는 회전 수는 그룹의 길이이므로 2*(N-i*2)+2*(M-i*2)-4
    이것을 R에 mod를 취하여 적용한다.
"""


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def partialLcm(a, b):
    return a * b / gcd(a, b)


def lcm(numbers):
    result = 0
    partial = numbers[0]

    for i in numbers:
        result = partialLcm(partial, i)

    return result


N, M, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

way = [M, N, M, N]

for i in range(min(N, M) // 2):
    rotate = int(R % (2 * (N - i * 2) + 2 * (M - i * 2) - 4))
    for _ in range(rotate):
        first = board[i][i]

        for step in range(i, M - i - 1):
            board[i][step] = board[i][step + 1]

        for step in range(i, N - i - 1):
            board[step][M - i - 1] = board[step + 1][M - i - 1]

        for step in range(M - i - 1, i, -1):
            board[N - i - 1][step] = board[N - i - 1][step - 1]

        for step in range(N - i - 1, i, -1):
            board[step][i] = board[step - 1][i]

        board[i + 1][i] = first

for i in range(N):
    for j in range(M):
        print(board[i][j], end=" ")
    print()

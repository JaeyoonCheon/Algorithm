"""
16926번 배열 돌리기 1
"""

N, M, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

way = [M, N, M, N]

for _ in range(R):
    groups = []

    for i in range(min(N, M) // 2):
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

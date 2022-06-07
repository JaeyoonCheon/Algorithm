"""
9663번 N-Queen

1.  기본적으로 N-Queen 문제는 가장 위 행에서부터 놓을 수 있는 퀸의 경우의 수를 백트래킹으로
    따지며서 내려가는 문제이다. 문제는 15*15 칸을 순회하며 놓을 때 다른 퀸과 겹치지 않는 지
    검사하는 단계를 포함하면 N^2 시간복잡도가 되어 비효율적인 코드가 되는 것이다.
    
2.  퀸을 어떤 행 row에 놓는 방법을 고르기 위한 N번 순회는 고정적이다.
    따라서, 놓은 퀸이 다른 퀸과 겹치지 않는 지 검사하는 단계에서 상수시간으로 시간을 줄여야 할 필요가 있다.
    
3.  우선, 이차원 배열로 표현한 체스판을 각 행에서 놓은 퀸의 열 위치만 저장하는 일차원 배열 형태로 변환할
    수 있다. 이것으로 수직적으로 검사하는 loop는 제거하였다.
    
4.  남은 것은 대각선에 놓인 퀸을 검사하는 단계인데, 우상향과 우하향 대각선 두 방향이 있다.
    처음에는 이것을 loop로만 검사해야 하는것으로 알았으나, 이차원 배열 상에서 좌표 위치를
    잘 살펴보면, 우상향하는 대각선에 위치하는 좌표들끼리는 행과 열의 합이 같으며,
    우하향하는 대각선에 위치하는 좌표들끼리는 행과 열의 차가 같다.
    이 성질을 이용해 각 대각선의 별도 위치 정보를 저장하는 배열을 만들고, 배열 3개에
    현재 좌표가 해당하는 위치 정보만 O(1) 시간에 확인할 수 있도록 최적화가 가능하다.
"""

N = int(input())

board = [[False] * N for _ in range(N)]

position = [False] * 3 * N

count = 0

position_cross_left = [False] * 3 * N
position_cross_right = [False] * 3 * N


def check(row, col):
    isCollision = False

    for i in range(row, -1, -1):
        if board[i][col] == True:
            isCollision = True

    nextRow, nextCol = row - 1, col - 1

    while True:
        if nextRow < 0 or nextRow > N - 1 or nextCol < 0 or nextCol > N - 1:
            break
        if board[nextRow][nextCol] == True:
            isCollision = True
        nextRow -= 1
        nextCol -= 1

    nextRow, nextCol = row - 1, col + 1

    while True:
        if nextRow < 0 or nextRow > N - 1 or nextCol < 0 or nextCol > N - 1:
            break
        if board[nextRow][nextCol] == True:
            isCollision = True
        nextRow -= 1
        nextCol += 1

    if isCollision:
        return False
    else:
        return True


def putQueen(row):
    global count

    if row == N:
        count += 1
        return

    for i in range(N):
        if check(row, i):
            board[row][i] = True
            putQueen(row + 1)
            board[row][i] = False


def putQueenOptimized(row):
    global count

    if row == N:
        count += 1
        return

    for i in range(N):
        if (
            position[i]
            or position_cross_left[N + i - row]
            or position_cross_right[i + row]
        ):
            continue

        position[i] = True
        position_cross_left[N + i - row] = True
        position_cross_right[i + row] = True

        putQueenOptimized(row + 1)

        position[i] = False
        position_cross_left[N + i - row] = False
        position_cross_right[i + row] = False


putQueenOptimized(0)
print(count)

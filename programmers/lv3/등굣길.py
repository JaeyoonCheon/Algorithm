"""
    lv.3 등굣길
    
    1.  dfs + dp로 해결가능하겠으나, 경로를 누적해가는 합의 법칙을 사용해 경우의 수를 더해가는 방식으로 풀이.
"""

MAX_MOD = 1000000007


def solution(m, n, puddles):
    answer = 0

    paths = [[0] * m for _ in range(n)]
    paths[0][0] = 1

    for row in range(n):
        for col in range(m):
            if [col + 1, row + 1] in puddles or (row, col) == (0, 0):
                continue
            if row == 0:
                paths[row][col] = (paths[row][col - 1]) % MAX_MOD
                continue
            if col == 0:
                paths[row][col] = (paths[row - 1][col]) % MAX_MOD
                continue
            paths[row][col] = (paths[row - 1][col] + paths[row][col - 1]) % MAX_MOD

    answer = paths[n - 1][m - 1]

    return answer


solution(4, 3, [[2, 2]])

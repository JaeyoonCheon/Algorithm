# 시간복잡도 스킬개수*보드 크기(N*M)
def doSkill(board, skill):
    degree = skill[5] * (-1) ** skill[0]
    fromX, fromY, toX, toY = skill[1], skill[2], skill[3], skill[4]

    for i in range(fromX, toX + 1):
        for j in range(fromY, toY + 1):
            board[i][j] += degree

    return board


# 누적합을 이용한 스킬개수 + 보드크기(N*M)풀이!
def makeSkills(board, skills):
    N, M = len(board), len(board[0])
    accBoard = [[0] * (M + 1) for _ in range(N + 1)]

    for skill in skills:
        degree = skill[5] * (-1) ** skill[0]
        fromX, fromY, toX, toY = skill[1], skill[2], skill[3], skill[4]

        accBoard[fromX][fromY] += degree
        accBoard[toX + 1][toY + 1] += degree
        accBoard[toX + 1][fromY] += -degree
        accBoard[fromX][toY + 1] += -degree

    for row in range(N + 1):
        for col in range(1, M + 1):
            accBoard[row][col] += accBoard[row][col - 1]

    for col in range(M + 1):
        for row in range(1, N + 1):
            accBoard[row][col] += accBoard[row - 1][col]

    for row in range(N):
        for col in range(M):
            board[row][col] += accBoard[row][col]

    return board


def solution(board, skills):
    answer = 0

    """
    for skill in skills:
        board = doSkill(board, skill)
    """
    board = makeSkills(board, skills)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    return answer


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skills = [
    [1, 0, 0, 3, 4, 4],
    [1, 2, 0, 2, 3, 2],
    [2, 1, 0, 3, 1, 2],
    [1, 0, 1, 3, 3, 1],
]

print(solution(board, skills))

"""
    lv.2 행렬 테두리 회전하기
    
    1.  (x1, y1) - (x2, y2) 범위의 사각형 최외각에 있는 수를 한 칸씩 시계방향으로 회전시키는 문제.
    2.  슬라이딩 퍼즐같이 수를 한 칸씩 4개의 꼭지점 기준으로 밀어 동작을 수행
    3.  시계 정방향으로 동작을 수행하면 한 변의 수를 밀 때마다 수를 하나씩 새로 저장해야 하는 번거로움이 존재
    4.  따라서, 수를 밀어올리는 동작을 시계 역방향으로 진행하여 가장 처음의 수만 저장하도록 작성.
"""


def rotate(mat, query):
    x1, y1, x2, y2 = query

    x1 = x1 - 1
    y1 = y1 - 1
    x2 = x2 - 1
    y2 = y2 - 1

    save = mat[x1][y1]
    minValue = save

    for i in range(x1, x2):
        mat[i][y1] = mat[i + 1][y1]
        minValue = min(minValue, mat[i][y1])

    for i in range(y1, y2):
        mat[x2][i] = mat[x2][i + 1]
        minValue = min(minValue, mat[x2][i])

    for i in range(x2, x1, -1):
        mat[i][y2] = mat[i - 1][y2]
        minValue = min(minValue, mat[i][y2])

    for i in range(y2, y1, -1):
        mat[x1][i] = mat[x1][i - 1]
        minValue = min(minValue, mat[x1][i])

    mat[x1][y1 + 1] = save

    return [mat, minValue]


def solution(rows, columns, queries):
    answer = []
    mat = [[0] * columns for _ in range(rows)]

    iter = 1
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = iter
            iter = iter + 1

    for query in queries:
        mat, minValue = rotate(mat, query)
        answer.append(minValue)

    return answer


print(solution(100, 97, [[1, 1, 100, 97]]))

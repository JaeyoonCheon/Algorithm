"""
12850번 본대 산책2

1.  가장 처음 풀이
    끝에서부터 역순으로 n초 전 위치에서 '정보과학관'으로 0초에 도착하도록 돌아가는 경우를 DP로 구하려했다.
    각 노드는 인접한 노드가 항상 정해져 있으므로, DP로 점화식을 세워 구할 수 있다고 보았으나 주어지는 시간 D가 10억이므로
    DP와 같은 N^2 풀이로는 불가능할 것으로 생각되었다.
    
2.  알고리즘 개선
    https://chinpa.tistory.com/149를 참고해 행렬 거듭제곱 문제로 치환할 수 있다는 것을 알게 되었다.
    여러 문제를 풀어 다른 문제에 적용할 수 있도록 노력이 필요할 듯 싶다.
"""

D = int(input())
MOD = 1000000007

case = (
    (0, 1, 1, 0, 0, 0, 0, 0),
    (1, 0, 1, 1, 0, 0, 0, 0),
    (1, 1, 0, 1, 1, 0, 0, 0),
    (0, 1, 1, 0, 1, 1, 0, 0),
    (0, 0, 1, 1, 0, 1, 1, 0),
    (0, 0, 0, 1, 1, 0, 0, 1),
    (0, 0, 0, 0, 1, 0, 0, 1),
    (0, 0, 0, 0, 0, 1, 1, 0),
)

idenMatrix = (
    (1, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 0),
    (0, 0, 0, 0, 0, 0, 0, 1),
)

idenCol = (
    (1,),
    (0,),
    (0,),
    (0,),
    (0,),
    (0,),
    (0,),
    (0,),
)


def multMatrix(A, B):
    rowA, colA = len(A), len(A[0])
    rowB, colB = len(B), len(B[0])

    temp = [[0 for _ in range(colB)] for _ in range(rowA)]

    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                temp[i][j] += (A[i][k] * B[k][j]) % MOD
                temp[i][j] %= MOD
        temp[i] = tuple(temp[i])

    return tuple(temp)


def getMatrixPower(matrix, power):
    if power == 1:
        return matrix

    half = getMatrixPower(matrix, power // 2)
    result = multMatrix(half, half)
    if power % 2 == 1:
        result = multMatrix(result, matrix)

    return result


result = multMatrix(getMatrixPower(case, D), idenCol)

print(result[0][0])

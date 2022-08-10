"""
11049번 행렬 곱셈 순서

1.  여러 행렬의 결합법칙에 따른 곱셈 연산 수가 최소가 되는 경우의 수를 찾는 문제.

2.  행렬의 곱의 연산은 항상 곱해지는 행렬의 행 * (중간 연결되는 부분의 열) * 곱하는 행렬의 열이다.
    이 때, 양 쪽의 곱해지는 행렬의 행과 곱하는 행렬의 열은 고정할 수 있으므로
    중간에 연결되는 기준점의 행렬의 열의 변화에 따라 그 곱을 계산해 줄 수 있다.
    
3.  위의 2번의 계산결과에 나뉘는 부분 양쪽의 행렬의 '최소 곱셈 연산 수'를 더해주어야 하는데
    이것을 저장해놓은 cache[i][j]는 i번째 행렬부터 j번째 행렬까지의 곱의 최소 곱셈 연산 수를 의미하며
    이것을 이용해 DP top-down 방식으로 해결했다.
"""

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

cache = [[float("INF")] * N for _ in range(N)]

for i in range(N):
    cache[i][i] = 0


def operation(rowA, common, colB):
    return rowA * common * colB


def mult(_from, _to):
    if cache[_from][_to] != float("INF"):
        return cache[_from][_to]

    cases = []

    for i in range(_from, _to):
        case = (
            operation(matrix[_from][0], matrix[i][1], matrix[_to][1])
            + mult(_from, i)
            + mult(i + 1, _to)
        )
        cases.append(case)

    cache[_from][_to] = min(cases)
    return cache[_from][_to]


print(mult(0, N - 1))

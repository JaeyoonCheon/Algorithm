"""
    lv.2 행렬의 곱셈
    
    1.  행렬 곱 구현
"""


def solution(arr1, arr2):
    n, m, l = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * l for _ in range(n)]

    for i in range(n):
        for j in range(l):
            temp = 0
            for k in range(m):
                temp = temp + arr1[i][k] * arr2[k][j]
            answer[i][j] = temp

    return answer

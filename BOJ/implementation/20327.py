"""
20327번 배열 돌리기 6

1.  배열 내부의 인덱스 조작이 간단한 듯 복잡한 문제.

2.  우선 단계 별 그룹으로 묶인 배열들의 시작점을 길이/단계로 나눠 
    (step * i) + k, (step * j) + l로 구해놓아야 한다.
    
3.  상하 반전과 좌우 반전은 각 그룹의 인덱스를 역순으로 저장하여 반환
    좌/우 회전 또한 행/열의 한쪽 인덱스를 역순으로 지정하여 저장 후 반환
    
4.  5~8번 연산은 step별 그룹으로 쪼개졌을 때 그룹 내부의 수는 변동 없이
    그룹 하나하나를 대상으로 1~4의 연산을 진행
    5~6번 연산은 전체를 뒤집은 뒤 그룹을 다시 뒤집으면 그룹 내부의 수는 원 순서대로 복귀
    7~8번 연산은 전체를 원하는 방향으로 돌린 뒤 그룹 내부의 수를 반대 방향으로 돌리면
    원 순서대로 복귀
"""

import sys


def operation(array, length, type, step):
    newArray = [[0] * length for _ in range(length)]

    if type == 1:
        for i in range(length // step):
            for j in range(length // step):
                for k in range(step // 2 + 1):
                    newArray[(step * i) + k] = array[(step * (i + 1)) - 1 - k]
                    newArray[(step * (i + 1)) - 1 - k] = array[(step * i) + k]

        return newArray

    elif type == 2:
        for i in range(length // step):
            for j in range(length // step):
                for k in range(step):
                    for l in range(step):
                        newArray[(step * i) + k][(step * j) + l] = array[
                            (step * i) + k
                        ][(step * (j + 1)) - 1 - l]

        return newArray

    elif type == 3:
        for i in range(length // step):
            for j in range(length // step):
                for k in range(step):
                    for l in range(step):
                        newArray[(step * i) + k][(step * j) + l] = array[
                            (step * i) + step - 1 - l
                        ][(step * j) + k]

        return newArray

    elif type == 4:
        for i in range(length // step):
            for j in range(length // step):
                for k in range(step):
                    for l in range(step):
                        newArray[(step * i) + k][(step * j) + l] = array[
                            (step * i) + l
                        ][(step * j) + step - 1 - k]

        return newArray

    elif type == 5:
        newArray = operation(array, length, 1, length)
        newArray = operation(newArray, length, 1, step)

        return newArray

    elif type == 6:
        newArray = operation(array, length, 2, length)
        newArray = operation(newArray, length, 2, step)

        return newArray

    elif type == 7:
        newArray = operation(array, length, 3, length)
        newArray = operation(newArray, length, 4, step)

        return newArray

    else:
        newArray = operation(array, length, 4, length)
        newArray = operation(newArray, length, 3, step)

        return newArray


N, R = map(int, sys.stdin.readline().split())

length = pow(2, N)

array = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]

for _ in range(R):
    type, level = map(int, sys.stdin.readline().split())

    step = pow(2, level)

    array = operation(array, length, type, step)

for i in range(length):
    for j in range(length):
        print(array[i][j], end=" ")
    print()

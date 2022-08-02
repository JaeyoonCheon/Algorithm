"""
2166번 다각형의 면적

Reference : https://gaussian37.github.io/math-algorithm-polygon_area/

1.  다각형의 연결된 순서대로 주어진 각 꼭지점의 좌표들을 이용해 다각형의 넓이를 구한다.

2.  연결된 두 좌표간의 determinant의 기하학적 의미는 벡터로 간주할 때
    선형 변환 후 두 벡터로 이루어지는 좁은 평행사변형이다.
    따라서 원점 기준 연결된 두 꼭지점이 이루는 벡터가 만들어내는 평행사변형의 넓이를
    모두 더한 후, 절대값을 취해주고(사분면에 따라 달라지기 떄문에)
    그 값을 반으로 나눠준다.(평행사변형의 절반은 필요 없다.)
"""

import sys

N = int(input())

path = [list(map(float, sys.stdin.readline().split())) for _ in range(N)]

length = len(path)

path.append(path[0])


def getDeterminant(length):
    sum = 0

    for i in range(length):
        det = path[i][0] * path[i + 1][1] - path[i + 1][0] * path[i][1]
        sum += det

    return abs(sum) / 2


result = getDeterminant(length)
print("{:.1f}".format(round(result, 1)))

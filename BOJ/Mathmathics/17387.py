"""
17387번 선분 교차 2

1.  단순 두 선분의 기울기 곱의 비교로만 접근하면 백만 단위의 곱으로 값이 나오므로
    분수 비교의 어려움이나 Round-off Error가 발생할 수 있어 다른 방식을 사용해야 하는 문제.

2.  주어진 선분을 벡터로 간주하면 그 벡터를 구성하는 점 간에 Cross product를 구할 수 있다.
    여기서 구하려는 d1~d4는 어떤 벡터의 양 끝 점에서 다른 벡터의 각각의 양 끝 점에 대한
    cross product의 결과물이다.

3.  구해진 d1~d4는 두 벡터간의 관계가 clockwise인 지, counter clockwise인 지 판별할 수 있어
    이것을 바탕으로 두 벡터가 교차하는지, 만나지 않는 지 알 수 있다.

4.  다만, 두 벡터가 한 점에서 만날 경우를 생각해야 하는데,
    d1~d4 중 하나의 값이 0이고 해당 determinant를 구성하는 세 벡터
    (한 벡터와 그 벡터의 양 끝~ 다른 벡터의 한 끝을 잇는 벡터)가 만나는 경우
    한 점에서 만난다는 것을 알 수 있다.(이 경우도 또한 교차한다고 간주.)

*   Determinant
    d1 = v(p1p3)xv(p1p4)
    d2 = v(p2p3)xv(p2p4)
    d3 = v(p3p1)xv(p3p2)
    d4 = v(p4p1)xv(p4p2)
"""

vector = [()]

for i in range(2):
    a, b, c, d = map(int, input().split())

    vector.append((a, b))
    vector.append((c, d))


def crossProduct(vectorA, vectorB):
    return vectorA[0] * vectorB[1] - vectorA[1] * vectorB[0]


def determinant(vectorA, vectorB, vectorC):
    CA = [vectorA[0] - vectorC[0], vectorA[1] - vectorC[1]]
    CB = [vectorB[0] - vectorC[0], vectorB[1] - vectorC[1]]

    cross = crossProduct(CA, CB)

    if cross > 0:
        return 1
    elif cross == 0:
        return 0
    else:
        return -1


def onLine(vectorA, vectorB, vectorC):
    if (
        vectorC[0] >= min(vectorA[0], vectorB[0])
        and vectorC[0] <= max(vectorA[0], vectorB[0])
        and vectorC[1] >= min(vectorA[1], vectorB[1])
        and vectorC[1] <= max(vectorA[1], vectorB[1])
    ):
        return True
    else:
        return False


def isCross(vector):
    d1 = determinant(vector[3], vector[4], vector[1])
    d2 = determinant(vector[3], vector[4], vector[2])
    d3 = determinant(vector[1], vector[2], vector[3])
    d4 = determinant(vector[1], vector[2], vector[4])

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    elif d1 == 0 and onLine(vector[3], vector[4], vector[1]):
        return True
    elif d2 == 0 and onLine(vector[3], vector[4], vector[2]):
        return True
    elif d3 == 0 and onLine(vector[1], vector[2], vector[3]):
        return True
    elif d4 == 0 and onLine(vector[1], vector[2], vector[4]):
        return True
    else:
        return False


if isCross(vector):
    print(1)
else:
    print(0)

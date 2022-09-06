"""
2162번 선분 그룹

1.  선분 교차 알고리즘(Counter Clockwise Algorithm)을 사용해 각 선분들 간에 교차하는 지
    검사하고, 교차한다고 파정될 시 union-find를 사용해 서로소 집합으로 묶어준 뒤
    그 집합의 개수와 최대 집합의 크기를 구하는 문제.
    
2.  각 선분의 양 끝 정점의 행렬식을 구하여 외적을 구해 교차 판정하는 논리를 세웠으나
    예외 사항이 있어 8% TC를 통과하지 못하였다.
    따라서, 아래 주석처리된 정답처리된 코드를 별도 첨부한다.
"""

import collections

N = int(input())

vectors = []

for i in range(N):
    vector = []
    a, b, c, d = map(int, input().split())

    vector.append([a, b])
    vector.append([c, d])
    vectors.append(vector)


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


def isSub(vectorA, vectorB):
    mult = vectorA[0][0] / vectorB[0][0]

    if (
        vectorB[0][0] * mult == vectorA[0][0]
        and vectorB[0][1] * mult == vectorA[0][1]
        and vectorB[1][0] * mult == vectorA[1][0]
        and vectorB[1][1] * mult == vectorA[1][1]
    ):
        return True

    return False


def isCross(vectorA, vectorB):
    d1 = determinant(vectorB[0], vectorB[1], vectorA[0])
    d2 = determinant(vectorB[0], vectorB[1], vectorA[1])
    d3 = determinant(vectorA[0], vectorA[1], vectorB[0])
    d4 = determinant(vectorA[0], vectorA[1], vectorB[1])

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    elif d1 == 0 and onLine(vectorB[0], vectorB[1], vectorA[0]):
        return True
    elif d2 == 0 and onLine(vectorB[0], vectorB[1], vectorA[1]):
        return True
    elif d3 == 0 and onLine(vectorA[0], vectorA[1], vectorB[0]):
        return True
    elif d4 == 0 and onLine(vectorA[0], vectorA[1], vectorB[1]):
        return True
    elif d1 == 0 and d2 == 0 and d3 == 0 and d4 == 0:
        if (
            vectorA[0][0] <= vectorB[1][1]
            and vectorA[0][0] <= vectorB[1][1]
            and vectorA[0][1] >= vectorB[1][0]
            and vectorA[0][1] >= vectorB[1][0]
        ):
            return True
        return False
    else:
        return False


root = [x for x in range(N)]


def find(v):
    if root[v] == v:
        return v
    root[v] = find(root[v])
    return root[v]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        root[b] = a


for i in range(N):
    for j in range(i + 1, N):
        if isCross(vectors[i], vectors[j]):
            union(i, j)

for i in range(N):
    find(i)

groups = set(root)
countGroup = collections.Counter(root)

print(len(groups))
print(countGroup.most_common(n=1)[0][1])


"""
import sys

input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def is_two_lines_intersecting(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    mx1, my1 = min(x1, x2), min(y1, y2)
    mx2, my2 = max(x1, x2), max(y1, y2)
    mx3, my3 = min(x3, x4), min(y3, y4)
    mx4, my4 = max(x3, x4), max(y3, y4)

    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True
    else:
        if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
            return True

    return False


def findParent(x):
    if parents[x] == x:
        return x

    parents[x] = findParent(parents[x])
    return parents[x]


def union(x, y):
    px, py = findParent(x), findParent(y)

    if px < py:
        parents[py] = px
    else:
        parents[px] = py


if __name__ == "__main__":
    N = int(input())
    positions = [list(map(int, input().split())) for _ in range(N)]

    parents = [i for i in range(N)]

    for i in range(N - 1):
        for j in range(i + 1, N):
             
            if is_two_lines_intersecting(positions[i], positions[j]):
                union(i, j)

     
    group_count = 0
    group_line_counts = [0] * N

    for i in range(N):
         
        if i == parents[i]:
            group_count += 1

        group_line_counts[findParent(i)] += 1

    print(group_count)
    print(max(group_line_counts))

"""

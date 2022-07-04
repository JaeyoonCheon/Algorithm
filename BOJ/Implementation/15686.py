"""
15686번 치킨 배달

1.  주어지는 값들은 지도상에 나타나 있는 격자이나, 이것을 집/치킨집으로 구분해 각각의 좌표값만을
    가지는 배열을 만들면 치킨집 A개 중 M개를 뽑아 그 치킨집들 - 집들 간 치킨거리의 최소값들을 구해
    총 치킨거리가 가장 작은 것을 구하면 된다.
"""

import itertools

N, M = map(int, input().split())

MAX_DIST = 3 * N
MAX_CHICKEN_DIST = 4 * N * N + 1

city = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
        else:
            continue


def chickenDist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])


closing = list(itertools.combinations(chicken, M))

minTotalChickenDist = MAX_CHICKEN_DIST

for i in closing:
    totalDist = 0
    for j in home:
        minDist = MAX_DIST
        for k in i:
            dist = chickenDist(j, k)
            if dist < minDist:
                minDist = dist
        totalDist += minDist

    if totalDist < minTotalChickenDist:
        minTotalChickenDist = totalDist

print(minTotalChickenDist)
